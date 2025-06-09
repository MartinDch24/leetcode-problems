class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        unique_chars = set()
        max_len = 0
        left = 0

        for right, char in enumerate(s):
            while char in unique_chars:
                unique_chars.remove(s[left])
                left += 1

            unique_chars.add(char)
            max_len = max(max_len, right - left + 1)

        return max_len