class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)  # Minimum possible carrying capacity
        right = sum(weights)  # Maximum possible carrying capacity

        while left <= right:
            mid = (left + right) // 2  # Candidate for carrying capacity
            d = 1  # Days it takes to ship all packages
            curr_weight = 0  # The current weight on the ship

            for w in weights:
                if curr_weight + w > mid:  # If we exceed the packages, increment days and reset curr_weight
                    d += 1
                    curr_weight = 0
                curr_weight += w

            if d <= days:  # If we shipped them too fast, decrease right
                right = mid - 1
            else:  # If we were too slow, increase left
                left = mid + 1

        return left  # Last valid candidate