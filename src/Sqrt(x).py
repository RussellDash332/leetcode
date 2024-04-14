class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        t = 0
        while t * t <= x:
            t += 1
        return t - 1
