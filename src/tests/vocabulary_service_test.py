import unittest
from services.vocabulary_service import VocabularyService
from services.trie import Trie


class TestVocabularyService(unittest.TestCase):
    def test_create_vocabulary(self):
        vocabulary_service = VocabularyService("sanasto.csv")
        vocabulary = vocabulary_service.create_vocabulary()
        self.assertIsInstance(vocabulary, Trie)

    def test_read_file(self):
        vocabulary_service = VocabularyService("sanasto.csv")
        words = vocabulary_service.read_file()
        self.assertEqual(len(words), 40203)
        
