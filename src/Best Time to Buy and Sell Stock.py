class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lo, hi = 10**4, 0
        for p in prices:
            lo = min(lo, p)
            hi = max(hi, p - lo)
        return hi
