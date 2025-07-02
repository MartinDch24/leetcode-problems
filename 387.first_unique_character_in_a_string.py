from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq_dict = Counter(s) # {<character1>: <times it appears>, ...}

        for i in range(len(s)):
            if freq_dict[s[i]] == 1:    # Check if the character so far appears only 1 (that makes it the first non-repeating)
                return i

        return -1