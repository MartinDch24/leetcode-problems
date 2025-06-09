class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_of_nums = sum(nums)

        if sum_of_nums % 2 != 0:
            return False

        target = sum_of_nums // 2

        sums = set([0])

        for n in nums:
            current_sums = set(sums)
            for s in current_sums:
                if s + n <= target:
                    sums.add(s + n)

            if target in sums:
                return True

        return target in sums