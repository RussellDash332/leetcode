class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0]*(amount+1) for _ in coins + [-1]]
        for i in range(len(dp)):
            dp[i][0] = 1
        coins = sorted(coins)
        for i in range(1, len(coins)+1):
            for j in range(1, len(dp[0])):
                if j >= coins[i-1]:
                    dp[i][j] += dp[i][j-coins[i-1]]
                dp[i][j] += dp[i-1][j]
        return dp[-1][amount]
