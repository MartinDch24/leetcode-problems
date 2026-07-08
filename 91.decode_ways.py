class Solution:
    def numDecodings(self, s: str) -> int:
        n =len(s)
        # Check if the begining of the string is valid
        if not s or s[0] == "0":
            return 0
        elif n == 1:
            return 1

        # dp[i] = ways to decode a substring of length i
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            # Decode the last digit on its own
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            # Decode the last two digits together if they form a valid letter
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i-2]

        return dp[n]