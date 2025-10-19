class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n        # dp[i] = length of a LIS ending at i
        count = [1] * n     # count[i] = number of LIS ending at i

        for i in range(n):
            for j in range(i):
                # Check whether we can use nums[i] to extend a LIS ending at nums[j]
                if nums[j] < nums[i]:
                    # If extending from nums[j] gives a strictly longer subsequence, update dp[i]
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        # inherit the number of ways to reach a LIS ending at nums[i] from nums[j], since one comes right after the other
                        count[i] = count[j]
                    # If the new length is the same as the largest we've found so far
                    elif dp[j] + 1 == dp[i]:
                        # Add the count of LIS ending at nums[j] to count[i]
                        count[i] += count[j]

        # Find the length of LIS overall
        longest = max(dp)
        # Return the total count of LIS with that length
        return sum(count[i] for i in range(n) if dp[i] == longest)