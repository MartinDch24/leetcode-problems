class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # dp[i][j] = <Min number of steps to make word1[:i] into word2[:j]>
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        # If word2 is empty, delete all characters of word1
        for i in range(n+1):
            dp[i][0] = i
        # Vice versa for word2
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # If the characters don't match, delete either from word1 or word2
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[n][m]