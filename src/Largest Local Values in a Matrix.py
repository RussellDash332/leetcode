class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[max(grid[i+di][j+dj] for di in range(3) for dj in range(3)) for j in range(len(grid[0])-2)] for i in range(len(grid)-2)]