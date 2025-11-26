#Resolved
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)  # Smallest possible sum
        right = sum(nums)  # The largest possible sum

        while left <= right:
            mid = (left + right) // 2  # Candidate largest subarray sum

            pieces = 1  # Subarrays we've split into
            curr_sum = 0  # The sum of the current subarray

            for n in nums:
                if n + curr_sum <= mid:
                    curr_sum += n  # Add to the current subarray
                else:
                    pieces += 1  # Increase pieces and start a new subarray sum
                    curr_sum = n

            # If we have less pieces than we can, we decrease mid, by reducing right
            if pieces <= k:
                right = mid - 1
            # Otherwise increase mid, by increasing left
            else:
                left = mid + 1

        return left  # Last valid value