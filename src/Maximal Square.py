class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not i or not j: dp[i][j] = int(matrix[i][j])
                else: dp[i][j] = int(matrix[i][j])*(1+min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]))
        return max(map(max, dp))**2