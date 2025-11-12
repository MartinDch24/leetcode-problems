class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        # Every time we merge piles, we get n - (k-1) piles
        # We can just pull aside 1 pile and get n-1, which we try to divide by k-1
        # If it is divisible, then we will have 1 final pile in the end
        # Otherwise the split is impossible
        if (n - 1) % (k - 1) != 0:
            return -1

        # dp[i][j] = the lowest cost to merge the piles in the interval from [i;j]
        # into a number of piles, valid for future merges
        dp = [[0] * n for _ in range(n)]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # Start ranges from length k
        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Find the split, where it will be cheapest to merge piles from i to m and the piles from m+1 to j
                # m increases in steps of k-1 to keep subintervals reducable to 1 pile
                dp[i][j] = min(dp[i][m] + dp[m + 1][j] for m in range(i, j, k - 1))

                # If the current amount of piles can be reduced the 1,
                # we add the cost of merging the interval [i; j] to dp[i][j]
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]

        return dp[0][n - 1]