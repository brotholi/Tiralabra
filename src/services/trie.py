ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzªµºÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑŃÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñńòóôõöøùúûüýþÿ0123456789šžωá,.!?;:'\"()[]-_*/+=%$&#|-> "


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
        self.children = [None]*len(ALPHABET)
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

    def add(self, word: str) -> None:
        """Metodi, joka lisää sanan trie-tietorakenteeseen

        Args:
            word (str): lisättävä sana
        """
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
        """Metodi, joka etsii sanan trie-tietorakenteesta

        Args:
            word (str): etsittävä sana

        Returns:
            bool: palauttaa True, jos sana löytyy, muuten False
        """
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