class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from heapq import *
        dp = [[10**6]*len(grid) for _ in range(len(grid))]
        dp[0] = grid[0]
        for i in range(1, len(grid)):
            t = list(dp[i-1]); heapify(t)
            for j in range(len(grid)):
                a, b = heappop(t), heappop(t)
                if a == dp[i-1][j]: dp[i][j] = min(dp[i][j], b+grid[i][j])
                else: dp[i][j] = min(dp[i][j], a+grid[i][j])
                heappush(t, a), heappush(t, b)
        return min(dp[-1])