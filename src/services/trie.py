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
            list: lista sanoista, jotka löytyivät
        """
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return []

        self.content = []
        self._dfs(node, word[:-1])
        return self.content

    def _dfs(self, node, prev):
        """Metodi, joka suorittaa syvyyshaun trie-tietorakenteessa

        Args:
            node (Node): solmu, josta haun aloitetaan
            prev (str): edellinen kirjain
        """
        if node.end_of_word:
            self.content.append(prev + node.letter)

        for child in node.children.values():
            self._dfs(child, prev + node.letter)

    def get_trie_content(self):
        """Metodi, joka palauttaa koko trie-tietorakenteen sisällön

        Returns:
            list: trie-tietorakenteen sisältö
        """
        self.content = []
        self._dfs(self.root, "")
        return self.content
