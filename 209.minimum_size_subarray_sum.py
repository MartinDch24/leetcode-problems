class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = float('inf')
        l = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]

            # Shrink window while the total sum is valid
            while total >= target:
                min_len = min(min_len, r-l+1)
                total -= nums[l]
                l += 1

        return min_len if min_len < float('inf') else 0