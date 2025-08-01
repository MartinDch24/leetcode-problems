class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7

        even_positions = (n + 1) // 2
        odd_positions = n // 2

        return pow(5, even_positions, mod) * pow(4, odd_positions, mod) % mod
