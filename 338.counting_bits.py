class Solution:
    def countBits(self, n: int) -> list[int]:
        '''
        Every time we hit a power of 2 as a number (2,4,8, etc.) a new leading bit gets added and all others get reset to 0.
        Then the new numbers begin being formed like the numbers before that new leading 1,
        so we can reuse those past numbers to make the new ones.
        '''
        dp = [0] * (n + 1)
        offset = 1  # The current power of 2 we're on

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i

            dp[i] = dp[i - offset] + 1

        return dp