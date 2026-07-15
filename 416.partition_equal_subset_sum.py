#Resolved - 2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        # If the sum can't be divided in 2 then we know we can't form 2 subsets with equal sums
        if total % 2 != 0:
            return False
        
        # We just need half the sum to prove that it can be divided in 2
        goal = total // 2
        # dp[i] = <can we form a subset from nums with a sum of i>
        dp = [False] * (goal+1)
        dp[0] = True
        
        for num in nums:
            for i in range(goal, num-1, -1):
                if i - num < 0:
                    continue
                if dp[i - num]:
                    dp[i] = True
        
        return dp[goal]