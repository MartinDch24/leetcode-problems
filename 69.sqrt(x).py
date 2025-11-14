#Resolved
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:   # If x is 0 or 1, we can just return it imidietly
            return x

        left, right = 1, x // 2 # We use binary search, starting with 1 as the left and the x//2 as the right, since that's the largest possible value for the square root of x
        while left <= right:
            mid = (left + right) // 2   # Compare mid² with x to see if it’s too small, too large, or exact
            if mid * mid == x:
                return mid
            elif mid * mid < x: # If the value is less, we move the left pointer up
                left = mid + 1
            else:               # If the value is more, we move the right pointer down
                right = mid - 1
        # Loop ends when left > right.
        # At this point:
        # - left is the smallest integer such that left^2 > x
        # - right is the largest integer such that right^2 <= x
        # Therefore, right is exactly the integer part (floor) of sqrt(x).
        return right