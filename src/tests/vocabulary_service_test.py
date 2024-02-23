import unittest
from unittest.mock import Mock
import random
from services.vocabulary_service import VocabularyService
from services.trie import Trie
from services.damerau_levenshtein import DamerauLevenshtein


class TestVocabularyService(unittest.TestCase):
    def setUp(self):
        self.create_test_file()
        self.trie_mock = Mock(wraps=Trie())
        self.damerau_levenshtein_mock = Mock(wraps=DamerauLevenshtein())
        self.vocabulary_service = VocabularyService(
            "src/data/sanasto_test.txt", self.trie_mock, self.damerau_levenshtein_mock)
        self.added_random_words = []

    def create_test_file(self):
        with open("src/data/sanasto_test.txt", "w") as file:
            file.write("kissa\nkoira\nkana\nkaali\nkarpalo\nkala\n")
        
    def tearDown(self) -> None:
        open("src/data/sanasto_test.txt", 'w').close()
        
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
        random_word = ''.join(random.choices(
            'abcdefghijklmnopqrstuvwxyz', k=5))
        self.assertTrue(
            self.vocabulary_service.add_word_to_vocabulary(random_word))
        self.trie_mock.add.assert_called_with(random_word)

    def test_add_existing_word_to_vocabulary(self):
        self.assertFalse(
            self.vocabulary_service.add_word_to_vocabulary("kissa"))

    def test_parse_text(self):
        self.assertEqual(self.vocabulary_service.parse_text(
            "kissa koira"), ["kissa", "koira"])
        self.assertEqual(self.vocabulary_service.parse_text(
            "kissa, koira! moi"), ["kissa,", "koira!", "moi"])

    def test_parse_text_with_none(self):
        self.assertEqual(self.vocabulary_service.parse_text(None), [])

    def test_combine_text(self):
        self.assertEqual(self.vocabulary_service.combine_text(
            ["kissa", "koira"]), "kissa koira")

    def test_combine_text_with_empty_list(self):
        self.assertEqual(self.vocabulary_service.combine_text([]), "")

    def test_fix_typos(self):
        self.assertEqual(self.vocabulary_service.fix_typos(
            ["kisda", "koire"])[0], ["kissa", "koira"])
        self.assertEqual(self.vocabulary_service.fix_typos(
            ["kisda,", "koiru,", "kalak."])[0], ["kissa,", "koira,", "kala."])
        self.assertEqual(self.vocabulary_service.fix_typos(
            ["kissantassu", "ja", "koira"])[0], ["kissantassu", "ja", "koira"])
        
    def test_fix_typos_with_words_that_can_be_corrected_does_not_return_unable_to_correct(self):
        self.assertFalse(self.vocabulary_service.fix_typos(["kissa", "koira"])[1])
        self.assertFalse(self.vocabulary_service.fix_typos(
            ["kisda,", "koiru,", "kalak."])[1])
        self.assertTrue(self.vocabulary_service.fix_typos(
            ["kissantassu", "ja", "koira"])[1])
        
    def test_fix_typos_with_words_that_cannot_be_corrected_returns_unable_to_correct(self):
        self.assertTrue(self.vocabulary_service.fix_typos(["aaaaaaaaa"])[1])
        self.assertTrue(self.vocabulary_service.fix_typos(["hei", "asdfghjkl"])[1])

    def test_fix_typos_with_empty_list(self):
        self.assertEqual(self.vocabulary_service.fix_typos([])[0], [])
        self.assertTrue(self.vocabulary_service.fix_typos([])[1])

    def test_fix_typos_with_none(self):
        self.assertEqual(self.vocabulary_service.fix_typos(None)[0], [])
        self.assertTrue(self.vocabulary_service.fix_typos(None)[1])
