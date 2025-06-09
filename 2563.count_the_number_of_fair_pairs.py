class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        n = len(nums) - 1

        def below_target(target):
            l = 0
            r = n
            count = 0

            while l < r:
                if nums[l] + nums[r] <= target:
                    count += r - l
                    l += 1
                else:
                    r -= 1

            return count

        return below_target(upper) - below_target(lower - 1)