import unittest
import random
from services.vocabulary_service import VocabularyService
from services.trie import Trie


class TestVocabularyService(unittest.TestCase):
    def setUp(self):
        self.vocabulary_service = VocabularyService("sanasto.csv")

    def test_find_similar_words(self):
        similar_words = self.vocabulary_service.find_similar_words("kisda")
        self.assertIn("kissa", similar_words)
        self.assertIn("kiska", similar_words)
        self.assertIn("kisa", similar_words)

    def test_find_similar_words_with_empty_string(self):
        similar_words = self.vocabulary_service.find_similar_words(None)
        self.assertEqual(similar_words, [])

    def test_find_similar_words_with_none(self):
        similar_words = self.vocabulary_service.find_similar_words("")
        self.assertEqual(similar_words, [])

    def test_find_word_in_vocabulary(self):
        self.assertTrue(
            self.vocabulary_service.find_word_in_vocabulary("kissa"))
        
    def test_add_word_to_vocabulary(self):
        self.assertFalse(
            self.vocabulary_service.add_word_to_vocabulary("Käärijä"))
        random_word = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        self.assertTrue(
            self.vocabulary_service.add_word_to_vocabulary(random_word))
    
    def test_add_word_to_vocabulary_with_none(self):
        self.assertFalse(
            self.vocabulary_service.add_word_to_vocabulary(None))
    