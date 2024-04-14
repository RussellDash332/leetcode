from itertools import permutations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        s = set(range(1, n+1))
        if k <= n//2:
            tup = lambda x: tuple(sorted(x))
            return set(map(tup, permutations(s, k)))
        else:
            tup = lambda x: tuple(sorted(s-set(x)))
            return set(map(tup, permutations(s, n-k)))
