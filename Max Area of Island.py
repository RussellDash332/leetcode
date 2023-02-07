class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.size = [1 for _ in range(N)]

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
                self.size[x] += self.size[y]
            else:
                self.p[x] = y
                self.size[y] += self.size[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        u = UFDS(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                        if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj]:
                            u.union(i*n+j,(i+di)*n+j+dj)
        best = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]: best = max(best, u.size[i*n+j])
        return best
