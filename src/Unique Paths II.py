class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i]: break
            dp[0][i] = 1
        for i in range(m):
            if obstacleGrid[i][0]: break
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]: dp[i][j] = 0
                else: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
