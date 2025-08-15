class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return ( n > 0   # The number has to be positive
        and (n & (n-1)) == 0    # We need to check whether the number is a power of 2, so the last condition can work.
                                # All powers of 2, bitwise, are a 1, followed by 0s (2 = 10, 4 = 100, ...)
                                # If we subtract 1 from a power of 2, all of the bits get reversed
                                # And if we do a bitwise AND on both numbers the result should be 0 (example: 4(100) - 1(001) = 3(011)).
                                # The bitwise AND requires both bits to be 1s, otherwise it returns 0 for the given bit position
        and (n-1) % 3 == 0 ) # All powers of 4, subtracted by 1 are divisible by 3
        # 4^k = (1+3)^k = 1 + (1! / (k!*(1-k)!))*3 + (2! / (k!*(2-k)!))*3^2 + 3^k
        # I am expanding (1+3)^k with the binomial theorem and the idea is that all of the addends are divisible by 3, except for the 1, which proves that 4^k - 1 is divisible by 3.