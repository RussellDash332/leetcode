class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def p(x, n):
            if n == 0:
                return 1
            if n % 2:
                return x * p(x, n - 1)
            return p(x, n // 2)**2
        
        if n < 0:
            return p(1/x, -n)
        return p(x, n)
