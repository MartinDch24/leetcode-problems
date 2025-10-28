class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [
            1]  # Pad the interval with 1s, since the out of bounds indeces are assumed to have a value of 1

        n = len(nums)  # The length of the padded array
        dp = [[0] * n for _ in range(
            n)]  # dp[i][j] = most coins we can collect in the interval (i, j), where are i and j are not inclusive

        for size in range(2, n):  # Distance between the left and right end of intervals (start from the smallest ones)
            # Left index
            for i in range(n - size):
                # Right index
                j = i + size

                # Take the max possible value of popping balloon k, where k is between i and j, then add the intervals (i, k) and (k, j) to the sum
                # We use default=0 in case there are no valid k's
                dp[i][j] = max((dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j] for k in range(i + 1, j)), default=0)

        return dp[0][n - 1]  # Return the full interval from 0 to n-1