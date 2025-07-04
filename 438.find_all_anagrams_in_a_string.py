from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)

        p_freq = Counter(p)  # {<char>: <times it appears>, ...} for p
        freq_window = Counter(s[:m])  # {<char>: <times it appears>, ...} for the first m characters of s
        result = []

        for i in range(m, n):
            if freq_window == p_freq:  # If frequencies match, the substring is an anagram of p
                result.append(i - m)

            freq_window[s[i - m]] -= 1  # Remove leftmost character
            if freq_window[s[i - m]] == 0:
                del freq_window[s[i - m]]

            freq_window[s[i]] += 1  # Add new character, to continue sliding the window right

        if freq_window == p_freq:  # Check after the last move in the loop
            result.append(n - m)

        return result