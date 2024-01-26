import unittest
from services.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.add("kissa")
        self.trie.add("koira")
        self.trie.add("kana")

    def test_search(self):
        self.assertTrue(self.trie.search("kissa"))
        self.assertTrue(self.trie.search("koira"))
        self.assertTrue(self.trie.search("kana"))
        self.assertFalse(self.trie.search("kissa "))
        self.assertFalse(self.trie.search("kiss"))
        self.assertFalse(self.trie.search("koir"))
        self.assertFalse(self.trie.search("kan"))
        self.assertFalse(self.trie.search("k"))
        self.assertFalse(self.trie.search(""))

    def test_add_unknown_character(self):
        self.trie.add("チ")
        self.assertFalse(self.trie.search("チ"))

        