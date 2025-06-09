class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_len = 0

        def expandAroundCenter(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(n):
            substr1 = expandAroundCenter(i, i)
            substr2 = expandAroundCenter(i, i + 1)

            if len(longest) < len(substr1):
                longest = substr1
            if len(longest) < len(substr2):
                longest = substr2

        return longest