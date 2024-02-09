import unittest
from unittest.mock import Mock
import random
from services.vocabulary_service import VocabularyService
from services.trie import Trie
from services.damerau_levenshtein import DamerauLevenshtein


class TestVocabularyService(unittest.TestCase):
    def setUp(self):
        self.trie_mock = Mock(wraps=Trie())
        self.damerau_levenshtein_mock = Mock(wraps=DamerauLevenshtein())
        self.vocabulary_service = VocabularyService("sanasto_test.csv", self.trie_mock, self.damerau_levenshtein_mock)
    
    def test_find_similar_words_with_none(self):
        similar_words = self.vocabulary_service.find_similar_words(None)
        self.damerau_levenshtein_mock.distance.assert_not_called()
        self.assertEqual(similar_words, [])

    def test_find_similar_words(self):
        self.vocabulary_service.find_similar_words("kisda")
        self.damerau_levenshtein_mock.distance.assert_called()

    def test_find_similar_words_with_empty_string(self):
        similar_words = self.vocabulary_service.find_similar_words("")
        self.damerau_levenshtein_mock.distance.assert_not_called()
        self.assertEqual(similar_words, [])

    def test_find_word_in_vocabulary(self):
        self.vocabulary_service.find_word_in_vocabulary("kissa")
        self.trie_mock.search.assert_called()

    def test_add_word_to_vocabulary_with_none(self):
        times_called = self.trie_mock.add.call_count
        self.assertFalse(
            self.vocabulary_service.add_word_to_vocabulary(None))
        self.assertEqual(self.trie_mock.add.call_count, times_called)

    def test_add_word_to_vocabulary(self):
        random_word = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        self.assertTrue(
            self.vocabulary_service.add_word_to_vocabulary(random_word))
        self.trie_mock.add.assert_called_with(random_word)
        
    def test_add_existing_word_to_vocabulary(self):
        self.assertFalse(
            self.vocabulary_service.add_word_to_vocabulary("kissa"))
        
        