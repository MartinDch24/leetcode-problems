class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i] = maximum score difference with stones stoneValue[i:]
        # dp[n] = 0 by deafault

        for i in range(n - 1, -1, -1):
            dp[i] = -float("inf")
            takeSum = 0  # The sum of the stones the current player is taking

            for t in [1, 2, 3]:
                if i + t > n:  # Index is out of bounds
                    break

                takeSum += stoneValue[i + t - 1]  # Take another stone
                dp[i] = max(dp[i], takeSum - dp[
                    i + t])  # dp[i+t], since the opponent will need to take from stones stoneValue[i+t:]

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"