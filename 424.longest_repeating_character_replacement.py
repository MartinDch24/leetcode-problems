#Resolved
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0

        seen_chars = defaultdict(int)  # {<char>: <how many times it appears in the current window>, ...}
        max_freq = 0  # The frequency of the character that appears the most

        for right, char in enumerate(s):
            seen_chars[char] += 1

            max_freq = max(max_freq, seen_chars[char])

            # Shrink the window until it can contain only 1 character after <=k replacements
            while (right - left + 1) - max_freq > k:
                seen_chars[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len