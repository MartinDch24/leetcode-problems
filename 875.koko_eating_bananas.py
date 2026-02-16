#Resolved - 2
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1    # Minimum value for k
        right = max(piles)  # Maximum value for k

        while left <= right:
            mid = (left+right) // 2
            hours_needed = 0

            # Check the current candidate for k
            for pile in piles:
                hours_needed += ceil(pile / mid)

            if hours_needed <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left