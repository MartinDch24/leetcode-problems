class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1    # Smallest viable divisor
        right = max(nums)   # Largest viable divisor

        while left <= right:
            mid = (left + right) // 2   # Candidate value for the divisor
            curr_sum = 0    # The sum of the numbers after division

            for n in nums:
                curr_sum += math.ceil(n / mid)

            # If the sum is bellow or equal to the threshold, try a smaller divisor
            if curr_sum <= threshold:
                right = mid-1
            # Otherwise, increase it
            else:
                left = mid+1

        return left # Left will be the last valid divisor