from itertools import permutations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        tup = lambda x: tuple(sorted(x))
        return set(map(tup, permutations(range(1,n+1), k)))
