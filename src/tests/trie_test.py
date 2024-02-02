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
        self.assertEqual(self.trie.search("k"), [
                         "kissa", "koira", "kana", "kaali", "karpalo"])
        self.assertEqual(self.trie.search("omena"), [])

    def test_get_trie_content(self):
        result = self.trie.get_trie_content()
        self.assertEqual(
            result, ["kissa", "koira", "kana", "kaali", "karpalo"])
        
    def test_search_with_empty_string(self):
        self.assertEqual(self.trie.search(""), [])
    
    def test_search_with_none(self):
        self.assertEqual(self.trie.search(None), [])

    def test_get_trie_content_with_empty_trie(self):
        trie = Trie()
        result = trie.get_trie_content()
        self.assertEqual(result, [])

    def test_get_trie_content_with_none(self):
        trie = Trie()
        result = trie.get_trie_content()
        self.assertEqual(result, [])

    def test_search_with_empty_trie(self):
        trie = Trie()
        self.assertEqual(trie.search("kissa"), [])
        self.assertEqual(trie.search("ka"), [])
        self.assertEqual(trie.search("k"), [])
        self.assertEqual(trie.search("omena"), [])
