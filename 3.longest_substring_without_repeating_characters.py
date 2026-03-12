#Resolved - 2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:   # Skip initializing all of the values bellow
            return 0

        max_len = 0
        seen = set() # Contains all unique characters in the sliding window
        left = 0

        for right in range(len(s)):
            # Shrink from the left, until the duplicate is removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # Add the new character to the set
            seen.add(s[right])

            max_len = max(max_len, right - left + 1)

        return max_len