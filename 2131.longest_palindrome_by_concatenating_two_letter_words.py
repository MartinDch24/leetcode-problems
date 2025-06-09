from collections import Counter


class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        counts = Counter(words)
        res = 0
        used_mid = True

        for w in counts:
            rev = w[::-1]

            if w == rev:
                pairs = counts[w] // 2
                res += pairs * 4
                if used_mid and counts[w] % 2:
                    res += 2
                    used_mid = False
            elif w < rev:
                pairs = min(counts[w], counts[rev])
                res += pairs * 4

        return res