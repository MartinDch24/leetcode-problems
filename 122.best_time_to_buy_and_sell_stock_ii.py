#Resolved
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # Profit so far
        curr_price = prices[0]  # The current price

        for price in prices:
            if curr_price < price:  # If the new price is higher than the current one - buy
                profit += price - curr_price
            curr_price = price  # Update the current price

        return profit