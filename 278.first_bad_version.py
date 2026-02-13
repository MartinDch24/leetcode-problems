# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1  # Smallest possilbe index of the bad version
        right = n  # Largest possible index of the bad version

        while left < right:
            mid = (left + right) // 2

            # The first bad version is at or before mid, so we don't shrink right = mid-1
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left