class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]   # Max profit for holding the stock we've bought
        sold = float('-inf')    # Max profit from selling today
        rest = 0    # Max profit from not holding a stock and not in cooldown

        for p in prices[1:]:
            # Save the previous values of the variables to form the new ones
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            # Either continue holding or buy today after having rested
            hold = max(prev_hold, prev_rest - p)
            # Sell today
            sold = prev_hold + p
            # Either continue resting or finish yesterday's cooldown
            rest = max(prev_rest, prev_sold)

        # The max profit is either from the rests or selling
        return max(sold, rest)
