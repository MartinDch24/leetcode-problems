class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        # dp[i][j] = <how many subsequences of s[:i] equal t[:j]>
        dp = [[0] * (m+1) for _ in range(n+1)]
        # if t is an empty string, all prefixes of s have the subsequence "" in them
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                # Ignore the current character of s
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    # Use the current character of s
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[n][m]