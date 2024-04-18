class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        A = 0; R = len(grid); C = len(grid[0])
        K = ((0, -1), (-1, 0), (1, 0), (0, 1))
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0: continue
                for di, dj in K:
                    if R>i+di>=0<=j+dj<C:
                        A += 1-grid[i+di][j+dj]
                    else:
                        A += 1
        return A