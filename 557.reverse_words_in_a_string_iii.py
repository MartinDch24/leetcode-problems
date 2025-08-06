class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(w[::-1] for w in s.split()) # split the string to get each word, reverse each word and join them with a space again