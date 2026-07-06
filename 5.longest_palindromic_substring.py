#Resolved
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #DP Solution:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0

        # All single characters are palindormes
        for i in range(n):
            dp[i][i] = True
            
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    # Check if the inside of the palindrome is either a single character or another pre-computed palindrome
                    if i == j-1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        length = j - i + 1

                        if length > max_len:
                            max_len = length
                            start = i
        return s[start:start + max_len]

        # n = len(s)
        # max_len = 0
        #
        # def expandAroundCenter(left, right):
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     return s[left + 1:right]
        #
        # longest = ""
        # for i in range(n):
        #     substr1 = expandAroundCenter(i, i)
        #     substr2 = expandAroundCenter(i, i + 1)
        #
        #     if len(longest) < len(substr1):
        #         longest = substr1
        #     if len(longest) < len(substr2):
        #         longest = substr2
        #
        # return longest