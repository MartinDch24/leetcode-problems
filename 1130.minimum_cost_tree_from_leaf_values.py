class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)] # dp[i][j] the minimum cost, given the array arr[i:j+1]
        max_leaf = [[0] * n for _ in range(n)]  # The largest leaf for the array arr[i][j]

        for i in range(n):
            max_leaf[i][i] = arr[i] # We start with the current leaf
            for j in range(i + 1, n):
                # Take the precomputed max value for the previous subarray and compare it to the current value, instead of iterating over the whole subarray every time
                max_leaf[i][j] = max(max_leaf[i][j - 1], arr[j])

        for length in range(2, n + 1):  # Build up all subarray length, starting from 2, so we can build the larger ones
            for i in range(n - length + 1):
                j = i + length - 1  # The end of the subarray
                # Add the cost of the left subtree, the right subtree and the cost to combine them with a new node
                dp[i][j] = min(
                    dp[i][k] + dp[k+1][j] + max_leaf[i][k] * max_leaf[k+1][j]
                    for k in range(i, j)
                )

        return dp[0][n-1]   # Return the answer for the whole given array