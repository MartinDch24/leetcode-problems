#Resolved
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=len)  # Take the shortest word in the lest and start from it as the longest possible prefix

        while not all(word.startswith(shortest_word) for word in strs): # While there are words that don't have shortest_word as a prefix
            shortest_word = shortest_word[:-1]  # Remove the last character of shortest word by slicing up to it

        return shortest_word