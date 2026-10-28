class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self._pref_sum = [0] * (len(nums) + 1)

        for i in range(1, len(self.nums) + 1):
            self._pref_sum[i] = self._pref_sum[i - 1] + self.nums[i - 1]

    @property
    def pref_sum(self):
        return self._pref_sum

    def sumRange(self, left: int, right: int) -> int:
        return self.pref_sum[right + 1] - self.pref_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)