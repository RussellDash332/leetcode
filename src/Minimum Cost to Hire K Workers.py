class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        from heapq import heappush, heappop
        pq = []; s = 0; a = 1e18
        for r, q in sorted((float(w)/q, q) for w, q in zip(wage, quality)):
            heappush(pq, -q)
            s += q
            if len(pq) > k: s += heappop(pq)
            if len(pq) == k: a = min(a, s*r)
        return a