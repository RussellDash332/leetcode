class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1: return 0
        n = len(grid)
        g = [{} for _ in range(n*n)]
        k = ((0, -1), (1, 0), (-1, 0), (0, 1))
        t = [i*n+j for i in range(n) for j in range(n) if grid[i][j]]
        dd = [-1]*n*n
        for ij in t: dd[ij] = 0
        for ij in t:
            i = ij//n; j = ij%n
            for di, dj in k:
                x = (i+di)*n+j+dj
                if n>i+di>-1<j+dj<n and dd[x] == -1: dd[x] = dd[ij]+1; t.append(x)
        for i in range(n):
            for j in range(n):
                for di, dj in k:
                    if n>i+di>-1<j+dj<n: x = (i+di)*n+j+dj; g[i*n+j][x] = min(dd[i*n+j], dd[x])
        from heapq import *
        s = 0; mst = [[] for _ in range(n*n)]
        pq = [(-g[s][t], t, s) for t in g[s]]; used = [0]*n*n; used[s] = 1; heapify(pq)
        while pq:
            w, u, p = heappop(pq)
            if used[u]: continue
            mst[p].append(u); used[u] = 1
            if u == n*n-1: break
            for v in g[u]: heappush(pq, (-g[u][v], v, u))
        q = [(0, dd[0])]
        for u, d in q:
            if d > dd[u]: d = dd[u]
            if u == n*n-1: return d
            for v in mst[u]: q.append((v, d))