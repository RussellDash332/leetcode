class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [10**9]*(len(cost)+2); dp[0] = dp[1] = 0
        for i in range(2, len(cost)+2):
            dp[i] = min(dp[i-1], dp[i-2])+cost[i-2]
        return min(dp[-1], dp[-2])