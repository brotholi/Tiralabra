import csv
from services.trie import Trie
from services.damerau_levenshtein import DamerauLevenshtein


class VocabularyService:
    """Luokka, joka luo tallentaa sanaston trie-tietorakenteeseen

    Atribuutit:
        trie: trie-tietorakenne
        file_path: sanaston tiedostopolku
    """

    def __init__(self, path):
        """_summary_

        Args:
            path (str): Tiedostopolku sanastoon, joka halutaan tallentaa trie-tietorakenteeseen
        """
        self.__damerau_levenshtein = DamerauLevenshtein()
        self.file_path = path
        self.__trie = self.create_vocabulary()

    def create_vocabulary(self):
        """Metodi, joka tallentaa tiedostossa olevan sanaston trie-tietorakenteeseen

        Returns:
            Trie-tietorakenteen, jossa on sanasto
        """
        trie = Trie()
        vocabulary_words = self._read_file()
        for word in vocabulary_words:
            trie.add(word)
        return trie

    def find_word_in_vocabulary(self, word):
        """Metodi, joka etsii sanan sanastosta

        Args:
            word (str): etsittävä sana

        Returns:
            bool: True, jos sana löytyy, muuten False
        """
        return self.__trie.search(word)

    def _read_file(self):
        """Metodi, joka lukee tiedostossa olevat sanat ja tallentaa ne listaan
        Returns:
            Lista, jossa on sanasto
        """
        with open(self.file_path, "r") as f:
            reader = csv.reader(f)
            words = []
            for row in reader:
                words.append(row[0])
        return words

    def find_similar_words(self, word):
        """Metodi, joka vertaa annettua sanaa sanaston sanoihin ja palauttaa sanat, joiden etäisyys on 1 tai 0

        Args:
            word (str): etsittävä sana

        Returns:
            list: lista sanoista, joiden etäisyys damerau-levenshtein-algoritmin mukaan on 1 tai 0
        """
        if not word:
            return []

        vocabulary = self.__trie.get_trie_content()
        similar_words = []
        for vocabulary_word in vocabulary:
            distance = self.__damerau_levenshtein.distance(word, vocabulary_word)
            if distance <= 1:
                similar_words.append(vocabulary_word)
        return similar_words
    
    def add_word_to_vocabulary(self, word):
        """Metodi, joka lisää sanan sanastoon

        Args:
            word (str): lisättävä sana

        Returns:
            bool: True, jos sana lisättiin, muuten False
        """
        if not word:
            return False
        if self.__trie.add(word):
            with open(self.file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([word])
            return True
        return False
                

