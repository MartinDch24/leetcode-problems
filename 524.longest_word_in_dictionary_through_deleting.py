class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word):
            j = 0  # Iterate over the word seperately
            for c in s:
                # Make sure the index is valid and compare the characters
                if j < len(word) and c == word[j]:
                    j += 1
            # We either found all characters of the word in s or we didn't
            return j == len(word)

        res = ""

        for word in dictionary:
            if is_subsequence(word):
                # -len(x) inverts the longer word to become shorter
                # Use min(), so we can get ascending lexicographical order
                res = min(res, word, key=lambda x: (-len(x), x))

        return res