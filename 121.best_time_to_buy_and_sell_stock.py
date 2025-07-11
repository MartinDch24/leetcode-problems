#Resolved
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]   # Minimum price found so far
        max_profit = 0  # Largest possible profit

        for price in prices:
            min_price = min(min_price, price)   # If the current price is less than min_price, it becomes the new min_price

            max_profit = max(max_profit, price-min_price)   # We check whether selling right now will yield more profit

        return max_profit