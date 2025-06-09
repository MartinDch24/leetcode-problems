from random import randint


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.arr_len = len(nums)

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.arr

    def shuffle(self):
        """
        :rtype: List[int]
        """
        res = list(self.arr)

        for i in range(self.arr_len):
            new_idx = randint(i, self.arr_len - 1)
            res[i], res[new_idx] = res[new_idx], res[i]

        return res
