import csv
from services.trie import Trie


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
        self.trie = Trie()
        self.file_path = path

    def create_vocabulary(self):
        """Metodi, joka tallentaa tiedostossa olevan sanaston trie-tietorakenteeseen

        Returns:
            Trie-tietorakenteen, jossa on sanasto
        """
        vocabulary_words = self.read_file()
        for word in vocabulary_words:
            self.trie.add(word)
        return self.trie

    def read_file(self):
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
