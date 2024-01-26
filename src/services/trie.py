ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzªµºÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑŃÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñńòóôõöøùúûüýþÿ0123456789šžωá,.!?;:'\"()[]-_*/+=%$&#|-> "


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = [None]*len(ALPHABET)
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node("")

    def add(self, word: str) -> None:
        node = self.root
        for letter in word:
            try:
                index = ALPHABET.index(letter)
                if not node.children[index]:
                    node.children[index] = Node(letter)
                node = node.children[index]
            except ValueError:
                continue
    
        node.end_of_word = True
        return

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            try:
                index = ALPHABET.index(letter)
                if not node.children[index]:
                    return False
                node = node.children[index]
            except ValueError:
                return False
        return node.end_of_word