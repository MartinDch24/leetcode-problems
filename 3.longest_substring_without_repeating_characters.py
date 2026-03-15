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

        #Hashmap solution:

        # last_index = defaultdict(lambda: -1)  # last_index[char] = <last index it was at>
        # left = 0  # Left end of the subarray
        # max_len = 0
        #
        # for right, char in enumerate(s):
        #     # If last_index[char]> left, then we have a duplicate we are removing with + 1
        #     left = max(left, last_index[char] + 1)
        #     last_index[char] = right
        #
        #     max_len = max(max_len, right - left + 1)
        #
        # return max_len