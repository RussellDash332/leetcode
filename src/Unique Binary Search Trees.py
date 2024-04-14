class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        for i in range(n):
            s = 0
            for j in range(i + 1):
                s += dp[j] * dp[i - j]
            dp.append(s)
            
        return dp[n]
