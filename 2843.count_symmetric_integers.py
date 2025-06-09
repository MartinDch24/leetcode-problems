class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        def sum_digits(num):
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            return sum

        sym_nums = 0

        for num in range(low, high + 1):
            str_num = str(num)
            num_len = len(str_num)
            if num_len % 2 != 0:
                continue

            half_len = num_len // 2
            if sum_digits(num % 10 ** (half_len)) == sum_digits(num // 10 ** (half_len)):
                sym_nums += 1

        return sym_nums