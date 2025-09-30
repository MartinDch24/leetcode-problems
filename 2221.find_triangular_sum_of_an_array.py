class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        # We need to repeat the process n-1 times to get to only 1 element left
        for i in range(n - 1):

            # The new array has length n - i and we subtract 1 so we can use j+1 as an index
            for j in range(n - i - 1):
                nums[j] = (nums[j] + nums[j + 1]) % 10

        # The first element in the array is the triangular sum of nums
        # The other elements are stale data from the previous iterations of the steps
        return nums[0]