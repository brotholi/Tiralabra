class Node:
    """Luokka, joka kuvaa trie-verkon yksittäistä solmua

    Atribuutit: 
        letter: solmun kirjain, joka on tyhjä merkkijono juurisolmussa
        children: solmun lapsisolmut
        end_of_word: boolean-arvo, joka kertoo, onko solmu sanan lopussa
    """

    def __init__(self, letter):
        """Luokan konstruktori, joka luo uuden solmun

        Args:
            letter (str): solmun kirjain
        """
        self.letter = letter
        self.children = {}
        self.end_of_word = False


class Trie:
    """Luokka, joka kuvaa trie-tietorakennetta ja johon voidaan tallentaan sanasto

    Atribuutit:
        root: trie-tietorakenteen juurisolmu
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden trie-tietorakenteen
        """
        self.root = Node("")
        self.content = []

    def add(self, word: str) -> None:
        """Metodi, joka lisää sanan trie-tietorakenteeseen

        Args:
            word (str): lisättävä sana
        """
        if not word:
            return

        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                next_node = Node(letter)
                node.children[letter] = next_node
                node = next_node

        node.end_of_word = True

    def search(self, word: str) -> bool:
        """Metodi, joka etsii sanan trie-tietorakenteesta

        Args:
            word (str): etsittävä sana

        Returns:
            bool: True, jos sana löytyy, muuten False
        """
        if not word:
            return False

        node = self.root

        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]

        return node.end_of_word

    def _dfs(self, node: Node, prev: str) -> None:
        """Metodi, joka suorittaa syvyyshaun trie-tietorakenteessa

        Args:
            node (Node): solmu, josta haun aloitetaan
            prev (str): edellinen kirjain
        """
        if node.end_of_word:
            self.content.append(prev + node.letter)

        for child in node.children.values():
            self._dfs(child, prev + node.letter)

    def get_trie_content(self) -> list:
        """Metodi, joka palauttaa kaikki trie-tietorakenteessa olevat sanat listana

        Returns:
            list: trie-tietorakenteen sisältö
        """
        self.content = []
        self._dfs(self.root, "")
        return self.content
