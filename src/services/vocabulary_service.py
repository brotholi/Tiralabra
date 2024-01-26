import csv
from services.trie import Trie

class VocabularyService:
    def __init__(self, path):
        self.trie = Trie()
        self.words = []
        self.file_path = path

    def create_vocabulary(self):
        self.read_file()
        for word in self.words:
            self.trie.add(word)
        return self.trie
    
    def read_file(self):
        with open(self.file_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                self.words.append(row[0])
        return
