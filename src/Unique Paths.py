class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        N = m+n-2
        r = min(m, n)-1
        res = 1
        for i in range(r):
            res *= N-i
            res //= i+1
        return res
