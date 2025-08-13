class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        largest_power_of_three = 3 ** 19    # The largest power of three that fits a 32-bit integer

        return n > 0 and largest_power_of_three % n == 0