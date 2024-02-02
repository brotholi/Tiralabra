class DamerauLevenshtein:
    """Luokka, joka tutkii etäisyyttä kahden merkkijonon välillä
    """

    def __init__(self):
        """"Luokan konstruktori, joka luo uuden DamerauLevenshtein-olion
        """

    def distance(self, word1: str, word2: str) -> int:
        """Metodi, joka tutkii etäisyyttä kahden merkkijonon välillä

        Args:
            words (list): lista, jossa on kaksi merkkijonoa

        Returns:
            int: etäisyys
        """

        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        inf = float("inf")
        distances = [[inf] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            distances[i][0] = i
        for j in range(len(word2) + 1):
            distances[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                cost = 1
                if word1[i-1] == word2[j-1]:
                    cost = 0
                distances[i][j] = min(distances[i][j - 1] + 1,
                                      distances[i - 1][j] + 1,
                                      distances[i - 1][j - 1] + cost)
                if i > 1 and j > 1 and word1[i - 1] == word2[j - 2] and word1[i - 2] == word2[j - 1]:
                    distances[i][j] = min(
                        distances[i][j], distances[i - 2][j - 2] + cost)

        return distances[len(word1)][len(word2)]
