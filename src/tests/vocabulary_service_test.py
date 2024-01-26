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
        vocabulary_service.read_file()
        self.assertEqual(len(vocabulary_service.words), 40203)
