import unittest
from services.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.add("kissa")
        self.trie.add("koira")
        self.trie.add("kana")
        self.trie.add("kaali")
        self.trie.add("karpalo")

    def test_search(self):
        self.assertEqual(self.trie.search("kissa"), ["kissa"])
        self.assertEqual(self.trie.search("ka"), ["kana", "kaali", "karpalo"])
        self.assertEqual(self.trie.search("k"), ["kissa", "koira", "kana", "kaali", "karpalo"])
        self.assertEqual(self.trie.search("omena"), [])

    def test_get_trie_content(self):
        result = self.trie.get_trie_content()
        self.assertEqual(result, ["kissa", "koira", "kana", "kaali", "karpalo"])

        