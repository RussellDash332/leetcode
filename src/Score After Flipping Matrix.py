class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n): grid[i][j] = 1-grid[i][j]
        for i in range(1, n):
            c = 0
            for j in range(m): c += grid[j][i]
            if 2*c < m:
                for j in range(m): grid[j][i] = 1-grid[j][i]
        a = 0
        for i in range(m):
            s = 0
            for j in range(n): s *= 2; s += grid[i][j]
            a += s
        return a