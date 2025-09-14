class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(b-a, 0) for a, b in zip(prices, prices[1:]))