class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        acc = 0

        for num in nums:
            # Use bitwise XOR to make sure that all elements that appear twice reduce each other's bits only to 0s and only the single number remains
            acc ^= num

        return acc