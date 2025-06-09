class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen_nums = set()

        for i in reversed(range(len(nums))):
            if nums[i] in seen_nums:
                return (i + 3) // 3
            seen_nums.add(nums[i])

        return 0