class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [1e9]*(amount+1)
        coins = set(coins)
        dp[0] = 0
        for amt in range(amount+1):
            if amt in coins:
                dp[amt] = 1
            for c in coins:
                if amt - c >= 0:
                    dp[amt] = min(dp[amt], dp[amt-c] + 1)
        if dp[-1] == 1e9: return -1
        return dp[-1]
