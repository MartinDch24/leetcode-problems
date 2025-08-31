class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        y = num
        while y*y > num:
            # We want to solve f(y) = y^2 - num = 0
            # Newton's method gives the iteration:
            #   y_next = (y + num / y) / 2
            # This quickly converges to sqrt(num).
            # We use integer division (//) to stay in integers
            # and avoid floating point precision issues.
            y = (y + num//y) // 2

        # When the loop ends, y is the floor of sqrt(num).
        # num is a perfect square only if y^2 == num.
        return y*y == num