class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def f(x):
            return sum((p+x-1)//x for p in piles) <= h
        lo, hi = 1, 10**9
        while lo < hi:
            mi = (lo+hi)//2
            if f(mi): hi = mi
            else: lo = mi+1
        return lo