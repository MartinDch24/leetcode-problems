class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = sum(nums[:k])    # The sum of the current subarray
        max_sum = curr_sum  # The largest possible sum of a subarray

        left = 0
        for right in range(k, len(nums)):
            curr_sum = curr_sum - nums[left] + nums[right]  # Remove the leftmost element, while adding the new one on the right
            left += 1

            if max_sum < curr_sum:  # If our new subarray's sum is greater than max_sum, max_sum gets its value
                max_sum = curr_sum

        return max_sum / float(k)   # We finally do the division by k for the sum to become an average and we use float on k, so that the answer can be a floating point number