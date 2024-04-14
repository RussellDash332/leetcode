class Solution(object):
    def __init__(self):
        self.h = {}

    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        def f(n, k):
            if (n, k) in self.h: return self.h[(n, k)]
            if k < 0 or k > n*(n+1)//2: return 0
            if k == 0 or k == n*(n+1)//2: return 1
            res = f(n, k-1) + f(n-1, k) - f(n-1, k-1-n)
            self.h[(n, k)] = res % MOD
            return self.h[(n, k)]
        return f(n-1, k)
