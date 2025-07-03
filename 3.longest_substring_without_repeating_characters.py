#Resolved
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:  # Skip initializing max_len, left and the set
            return 0

        unique_chars = set()  # Store all unique characters found so far
        max_len = 0

        left = 0  # The first index of the substring
        for right, c in enumerate(s):  # We call the index right, so left makes more sense
            while c in unique_chars:  # While new character is already in the substring
                unique_chars.remove(s[
                                        left])  # Start removing characters from the substring, left to right, until there no longer is a duplicate
                left += 1

            unique_chars.add(c)  # Finally add the new character, the previous instance of which we removed

            max_len = max(max_len, right - left + 1)  # We add +1, because left and right are indices

        return max_len