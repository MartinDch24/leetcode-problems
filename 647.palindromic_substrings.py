class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0

        for i in range(n):
            dp[i][i] = True
            res += 1
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # Check the start and end characters of the substring match
                if s[i] == s[j]:
                    # Check if the inside of the substring is a palindrome
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        res += 1

        return res