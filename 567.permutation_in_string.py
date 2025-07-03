from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)  # Length of s1
        m = len(s2)  # Length of s2

        if n > m:  # Can't be true if s1 is longer than s2
            return False

        s1_freq = Counter(s1)  # {<char1>: <it's count>} for s1
        freq_window = Counter(s2[:n])  # {<char1>: <it's count>} for the first n chars of s1
        # We will be moving this frequency window
        for i in range(n, m):
            if s1_freq == freq_window:  # If the dictionaries are identical, we've found a permutation of s1
                return True

            freq_window[s2[i - n]] -= 1  # Remove left character from substring
            if freq_window[s2[i - n]] == 0:
                del freq_window[s2[i - n]]

            freq_window[s2[i]] += 1  # Add right character to substring

        if s1_freq == freq_window:
            return True

        return False