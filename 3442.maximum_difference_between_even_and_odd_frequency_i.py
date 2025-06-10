from collections import Counter
class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        return max(v for v in freq.values() if v % 2 != 0) - min(v for v in freq.values() if v % 2 == 0)