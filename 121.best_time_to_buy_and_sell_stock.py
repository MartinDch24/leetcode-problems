#Resolved - 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]   # Smallest price so far
        max_profit = 0  # Largest possible profit

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price) # See if selling on the current day will yield a larger profit

        return max_profit