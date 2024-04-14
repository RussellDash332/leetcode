from heapq import *
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) frequency counting
        h = Counter(nums)
        # O(k) array creation
        pq = [(-b,a) for a,b in h.items()]
        heapify(pq) # O(n) heapify
        r = []
        # O(k log k) since there are at most k elements in PQ
        for _ in range(k): r.append(heappop(pq)[1])
        return r
