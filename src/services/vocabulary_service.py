import csv
from services.trie import Trie
from services.damerau_levenshtein import DamerauLevenshtein


class VocabularyService:
    """Luokka, joka vastaa sanaston käsittelystä

    Atribuutit:
        damerau_levenshtein (DamerauLevenshtein): luokka, joka tutkii etäisyyttä kahden merkkijonon välillä
        trie (Trie): trie-tietorakenne, johon sanasto tallennetaan
        file_path (str): tiedostopolku, jossa sanasto sijaitsee
    """

    def __init__(self, path, trie=Trie(), damerau_levenshtein=DamerauLevenshtein()):
        """_summary_

        Args:
            path (str): tiedostopolku, jossa sanasto sijaitsee
            trie (Trie, optional): trie-tietorakenne, johon sanasto tallennetaan. Defaults to Trie().
            damerau_levenshtein (DamerauLevenshtein, optional): luokka, joka tutkii etäisyyttä kahden merkkijonon välillä. Defaults to DamerauLevenshtein().    

        """
        self.damerau_levenshtein = damerau_levenshtein
        self.trie = trie
        self.file_path = path
        self.create_vocabulary()

    def create_vocabulary(self):
        """Metodi, joka tallentaa tiedostossa olevan sanaston trie-tietorakenteeseen
        """
        vocabulary_words = self._read_file()
        for word in vocabulary_words:
            self.trie.add(word.lower())
        return

    def find_word_in_vocabulary(self, word):
        """Metodi, joka etsii sanan sanastosta

        Args:
            word (str): etsittävä sana

        Returns:
            bool: True, jos sana löytyy, muuten False
        """
        return self.trie.search(word.lower())

    def _read_file(self):
        """Metodi, joka lukee tiedostossa olevat sanat ja tallentaa ne listaan
        Returns:
            Lista, jossa on sanasto
        """
        words = []
        with open(self.file_path, "r", encoding='UTF-8') as file:
            for row in file:
                words.append(row.strip())
        return words

    def find_similar_words(self, word, quick_fix=False):
        """Metodi, joka vertaa annettua sanaa sanaston sanoihin ja palauttaa sanat, joiden etäisyys on 1 tai 0.

        Args:
            word (str): etsittävä sana
            quick_fix (bool, optional): boolean-arvo, joka määrittää, palautetaanko vain yksi sana. Default-arvo on alse.

        Returns:
            list: lista sanoista, joiden etäisyys damerau-levenshtein-algoritmin mukaan on 1 tai 0
        """
        if not word:
            return []

        vocabulary = self.trie.get_trie_content()
        similar_words = []
        for vocabulary_word in vocabulary:
            distance = self.damerau_levenshtein.distance(
                word.strip().lower(), vocabulary_word)
            if distance <= 1 and len(vocabulary_word) >= 2:
                similar_words.append(vocabulary_word)
                if quick_fix:
                    return similar_words
        return similar_words

    def add_word_to_vocabulary(self, word):
        """Metodi, joka lisää sanan sanastoon

        Args:
            word (str): lisättävä sana

        Returns:
            bool: True, jos sana lisättiin eikä sanaa ollut ennestään sanastossa, muuten False
        """
        if not word:
            return False
        parsed_word = word.strip().lower()
        if not self.find_word_in_vocabulary(parsed_word):
            self.trie.add(parsed_word)
            with open(self.file_path, mode='a', encoding='UTF-8') as file:
                file.write(parsed_word + "\n")
            return True
        return False

    def parse_text(self, text):
        """Metodi, joka jakaa tekstin sanoiksi

        Args:
            text (str): jaettava teksti

        Returns:
            list: lista sanoista
        """
        if not text:
            return []

        return text.split()

    def combine_text(self, words):
        """Metodi, joka yhdistää sanat tekstiksi

        Args:
            words (list): lista sanoista

        Returns:
            str: yhdistetty teksti
        """
        if not words:
            return ""

        return " ".join(words)

    def fix_typos(self, words):
        """Metodi, joka korjaa tekstissä olevat kirjoitusvirheet
        Args:
            words (list): lista sanoista
        Returns:
            list: korjatut sanat
            bool: boolean-arvo, joka kertoo, voitiinko kaikki sanat korjata
        """
        if not words:
            return [[], True]

        corrected_words = []
        unable_to_correct = False

        for word in words:
            # Välimerkit talteen
            punctuation_mark = ""
            if word[-1] in [".", ",", "!", "?"]:
                punctuation_mark = word[-1]
                word = word[:-1]

            if len(word) > 1 and not self.find_word_in_vocabulary(word.lower()):
                similar_words = self.find_similar_words(word.lower(), True)
            # Sanastosta ei löytynyt läheistä sanaa, joten ei korjata
                if len(similar_words) == 0:
                    corrected_words.append(word + punctuation_mark)
                    unable_to_correct = True
                else:
                    corrected_words.append(similar_words[0] + punctuation_mark)

            # Sana löytyi sanastosta, joten ei korjata tai sana on yhden merkin mittainen
            else:
                corrected_words.append(word + punctuation_mark)

        return [corrected_words, unable_to_correct]
