#Resolved - 2
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ""

        to_find = Counter(t)
        have = Counter()
        unique_chars_found = 0

        min_window = float('inf')
        min_left = 0  # the left pointer of the smallest window we find
        left = 0
        for i in range(m):
            have[s[i]] += 1

            if have[s[i]] == to_find[s[i]]:
                unique_chars_found += 1

            if unique_chars_found == len(to_find.keys()):
                # Shrink as much as possible from the left, while preserving all characters of t
                while have[s[left]] > to_find[s[left]]:
                    have[s[left]] -= 1
                    left += 1

                if min_window > i - left + 1:
                    min_window = i - left + 1
                    min_left = left

        return s[min_left: min_left + min_window] if min_window != float('inf') else ""