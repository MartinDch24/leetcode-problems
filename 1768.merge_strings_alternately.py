class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []  # We'll save the characters in a list and join them at the end

        for c1, c2 in zip(word1,
                          word2):  # We use zip to iterate through the characters of both strings, but that will leave out the last characters of the longer strings
            res.append(c1)
            res.append(c2)

        res.extend(word1[
                   len(word2):])  # Doesn't matter which string is longer, since the other slice will simply be an empty string if the index is out of range
        res.extend(word2[len(word1):])

        return "".join(res)