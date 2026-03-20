#Resolved
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)  # {<char of t>: <how many times it appears in t>, ...}
        freq_window = Counter()  # {<char in current window>: <its count>}

        res = [-1, -1]  # [left, right] of the substring
        res_len = float('inf')  # the length of the substring

        # Each time we have enough units of a unique char, we add to char
        # We want to have enough of each unique char to satisfy need
        have, need = 0, len(freq_t)
        left = 0

        for right, char in enumerate(s):
            freq_window[char] += 1

            if char in freq_t and freq_window[char] == freq_t[char]:
                have += 1

            # Shrink the window, but keep it valid
            while have == need:
                # Check if we've found a shorter valid substring
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                curr = s[left]
                freq_window[curr] -= 1

                if curr in freq_t and freq_window[curr] < freq_t[curr]:
                    have -= 1
                left += 1

        if res_len == float('inf'):
            return ""
        return s[res[0]: res[1] + 1]
