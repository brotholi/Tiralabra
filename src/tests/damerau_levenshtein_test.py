import unittest
from services.damerau_levenshtein import DamerauLevenshtein


class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.damerau_levenshtein = DamerauLevenshtein()
        self.word1 = "kissa"
        self.word2 = "kissoja"

    def test_distance(self):
        self.assertEqual(self.damerau_levenshtein.distance(
            self.word1, self.word2), 2)
        self.assertEqual(
            self.damerau_levenshtein.distance("kissa", "kissa"), 0)
