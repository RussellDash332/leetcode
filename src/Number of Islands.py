class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]

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
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        u = UFDS(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                        if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj] == '1':
                            u.union(i*n+j,(i+di)*n+j+dj)
        land = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': land.add(u.find_set(i*n+j))
        return len(land)
