class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]

        for p in prices:
            if p < buy:
                buy = p
            if profit < p - buy:
                profit = p-buy

        return profit