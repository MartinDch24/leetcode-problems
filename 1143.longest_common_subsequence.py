class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # dp[i][j] = <longest common subsequence (LCS) for text1[:i] and text2[:j]>
        # Add an extra row, so dp[0][0] represents the LCS of no characters of text1 and no characters of text2
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Extend the previous dp state
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # If the characters don't match
                    # Discard one character from text1 or text2, choosing the option with the better LCS
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]