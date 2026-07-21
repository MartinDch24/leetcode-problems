class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # O(1) lookups
        wordSet = set(wordDict)

        # dp[i] = <can s[:i] be split into words from wordDict>
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                # If s is valid up to j, then check if s[j:i] is a validway to extend s[:j] 
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]