import unittest
from hypothesis import given, settings
import hypothesis.strategies as st
from services.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.add("kissa")
        self.trie.add("koira")
        self.trie.add("kana")
        self.trie.add("kaali")
        self.trie.add("karpalo")

    def test_add(self):
        self.assertTrue(self.trie.search("kissa"))
        self.assertTrue(self.trie.search("koira"))
        self.assertTrue(self.trie.search("kana"))
        self.assertTrue(self.trie.search("kaali"))
        self.assertTrue(self.trie.search("karpalo"))

    def test_add_with_none(self):
        self.trie.add(None)
        self.assertFalse(self.trie.search(None))

    def test_search(self):
        self.assertTrue(self.trie.search("kissa"))

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
        self.assertFalse(trie.search("kissa"))
        self.assertFalse(trie.search("koira"))
        self.assertFalse(trie.search(" "))

    @given(arvo=st.text(min_size=1, max_size=50))
    @settings(max_examples=1000)
    def test_search_with_hypothesis(self, arvo):
        self.assertFalse(self.trie.search(arvo))