class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Even if all the flowers bloomed instantly,
        # there aren't enough to form m bouquets of size k.
        if m > len(bloomDay) // k:
            return -1

        left = min(bloomDay)  # Minimum possible days
        right = max(bloomDay)  # Maximum possible days

        while left <= right:
            mid = (left + right) // 2  # Candidate value for the days we need
            curr_flowers_needed = k  # How many adjacent flowers until we can make a bouquet
            bouquets = 0  # Bouquets we made for mid days

            for d in bloomDay:
                # If the flower has bloomed, take it for the current bouquet
                if d <= mid:
                    curr_flowers_needed -= 1

                    # Check if we've made a bouquet
                    if not curr_flowers_needed:
                        bouquets += 1
                        curr_flowers_needed = k

                # If the current flower hasn't bloomed, then we reset the counter,
                # since we want the bouquets to be made from adjacent flowers
                else:
                    curr_flowers_needed = k

            # Not enough bouquets, so we increase the days
            if bouquets < m:
                left = mid + 1
            # Enough or too many bouquets, so we try to decrease the days
            else:
                right = mid - 1

        return left  # The smallest day for which forming m bouquets is possible