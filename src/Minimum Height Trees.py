class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        d = [-1]*n
        al = [[] for _ in range(n)]
        for a, b in edges: al[a].append(b); al[b].append(a)
        q = [(0, 0)]
        for u, x in q:
            if d[u] != -1: continue
            d[u] = x
            for v in al[u]: q.append((v, x+1))
        m = max(d)
        for i in range(n):
            if d[i] == m: s = i; break
        q = [(s, 0, -1)]
        d = [-1]*n; p = [-1]*n
        for u, x, y in q:
            if d[u] != -1: continue
            d[u] = x; p[u] = y
            for v in al[u]: q.append((v, x+1, u))
        m = max(d)
        l = [i for i in range(n) if d[i] == m]
        r = [0]*n
        for i in l:
            for _ in range(m//2): i = p[i]
            r[i] = 1
        for i in l:
            for _ in range(m-m//2): i = p[i]
            r[i] = 1
        return [i for i in range(n) if r[i]]