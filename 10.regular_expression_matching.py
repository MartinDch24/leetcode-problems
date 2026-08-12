#Resolved
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)
        m = len(s)
        # Can the pattern p[:i] match the string s[:j]
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(2, n+1, 2):
            if p[i-1] == "*":
                dp[i][0] = dp[i-2][0]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[i-1] == s[j-1] or p[i-1] == ".":
                    # Since characters match, see if the previous ones matched too 
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == "*":
                    # zero occurrences of the char in s
                    dp[i][j] = dp[i-2][j]

                    # one or more occurrences
                    if p[i-2] == s[j-1] or p[i-2] == ".":
                        dp[i][j] |= dp[i][j-1]
    
        return dp[n][m]