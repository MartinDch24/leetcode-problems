class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = "1"

        for _ in range(n - 1):
            curr_digit = num[0]
            counter = 0
            nth_num = []

            for digit in num:
                if curr_digit == digit:
                    counter += 1
                else:
                    nth_num.append(str(counter))
                    nth_num.append(curr_digit)

                    curr_digit = digit
                    counter = 1

            nth_num.append(str(counter))
            nth_num.append(curr_digit)
            num = "".join(nth_num)

        return num