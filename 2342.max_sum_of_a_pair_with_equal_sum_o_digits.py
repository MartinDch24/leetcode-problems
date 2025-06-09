class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # def sumDigits(n):
        #     sum = 0
        #     while n:
        #         sum += n % 10
        #         n //= 10
        #
        #     return sum
        #
        # sums = {}
        #
        # for i in range(len(nums)):
        #     i_num_digit_sum = sumDigits(nums[i])
        #     for j in range(i+1, len(nums)):
        #         if (i, j) not in sums:
        #             if i_num_digit_sum == sumDigits(nums[j]):
        #                 sums[i, j] = nums[i] + nums[j]
        #
        # return max(sums.values()) if sums else -1

        def sumDigits(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        sum_map = {}
        max_pair_sum = -1

        for num in nums:
            digit_sum = sumDigits(num)

            if digit_sum in sum_map:
                max_pair_sum = max(max_pair_sum, sum_map[digit_sum] + num)

            sum_map[digit_sum] = max(sum_map.get(digit_sum, 0), num)

        return max_pair_sum
