class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0  # Accumulating profit
        curr_price = prices[0]  # We save yesterday's price in a variable

        for price in prices:
            if price > curr_price:  # If today's price is higher than yesterday's we sell and add the profit
                res += price - curr_price
            curr_price = price

        return res