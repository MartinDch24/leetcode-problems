#Resolved - 2
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)    # Smallest feasible sum
        right = sum(nums)   # Largest possible sum

        while left <= right:
            mid = (left + right) // 2   # Candidate largest sum in a subarray

            curr = 0    # Current subarray sum
            splits = 1
            for n in nums:
                if curr + n > mid:
                    splits += 1
                    curr = 0
                curr += n

            # If we have too many splits, then we need a larger max sum
            if splits > k:
                left = mid+1
            else:
                right = mid-1

        return left # Left will hold the last valid max sum