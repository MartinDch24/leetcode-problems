class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)  # Answer array

        prefix = 1  # We multiply each number(currently 1) by the prefix so far, which is the product of all numbers up to nums[i]
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        # We do the same as the prefix but in reverse. Since each ans[i] gets multiplied by the product of the numbers up to it, we still skip multpling by nums[i], thus satisfying the problem description.
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans