from collections import deque

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        g = {}
        m, n = len(heights), len(heights[0])
        for i in range(m):
            for j in range(n):
                for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    if 0<=i+di<m and 0<=j+dj<n and heights[i][j] <= heights[i+di][j+dj]:
                        if i*n+j not in g:
                            g[i*n+j] = set()
                        g[i*n+j].add((i+di)*n+j+dj)
        g[m*n] = set()
        g[m*n+1] = set()
        for i in range(n):
            g[m*n].add(i)
            g[m*n+1].add((m-1)*n+i)
        for i in range(m):
            g[m*n].add(i*n)
            g[m*n+1].add((i+1)*n-1)

        q, v = deque([m*n]), set()
        p = set()
        while q:
            u = q.popleft()
            p.add((u//n, u%n))
            v.add(u)
            if u in g:
                for w in g[u]:
                    if w not in v:
                        q.append(w)

        q, v = deque([m*n+1]), set()
        a = set()
        while q:
            u = q.popleft()
            a.add((u//n, u%n))
            v.add(u)
            if u in g:
                for w in g[u]:
                    if w not in v:
                        q.append(w)

        return a & p
