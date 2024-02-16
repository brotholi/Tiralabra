import csv
from services.trie import Trie
from services.damerau_levenshtein import DamerauLevenshtein


class VocabularyService:
    """Luokka, joka luo tallentaa sanaston trie-tietorakenteeseen

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
            self.trie.add(word)
        return

    def find_word_in_vocabulary(self, word):
        """Metodi, joka etsii sanan sanastosta

        Args:
            word (str): etsittävä sana

        Returns:
            bool: True, jos sana löytyy, muuten False
        """
        return self.trie.search(word)

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

        vocabulary = self.trie.get_trie_content()
        similar_words = []
        for vocabulary_word in vocabulary:
            distance = self.damerau_levenshtein.distance(word, vocabulary_word)
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
        if self.trie.add(word):
            with open(self.file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([word])
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
        """
        if not words:
            return []

        corrected_words = []

        for word in words:
        # Make sure punctuation marks are preserved
            punctuation_mark = ""
            if word[-1] in [".", ",", "!", "?"]:
                punctuation_mark = word[-1]
                word = word[:-1]

            if not self.find_word_in_vocabulary(word):
                similar_words = self.find_similar_words(word)
        # No similar words were found, assume word is correct
                if len(similar_words) == 0:
                    corrected_words.append(word + punctuation_mark)
                else:
                    corrected_words.append(similar_words[0] + punctuation_mark)

        # Word was found in vocabulary, so it is correct            
            else:
                corrected_words.append(word + punctuation_mark)

        return corrected_words
    