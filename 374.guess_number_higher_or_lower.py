# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1    # Smallest possible guess
        right = n   # Largest possible guess

        # Use Binary search to find the number
        while left <= right:
            mid = (left + right) // 2

            res = guess(mid)

            if res == -1:
                right = mid-1
            elif res == 1:
                left = mid+1
            else:
                return mid
        return -1   # This line shouldn't be reached and just adds completeness