from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) # Build frequency maps for both strings and compare them ({char1: freq1, ...} and the same for the other string)