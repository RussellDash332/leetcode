class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """        
        dp = []
        for _ in range(len(rods) + 1):
            dp.append({})
        dp[0][0] = 0
        for i in range(len(rods)):
            for diff in dp[i]:
                dp[i + 1][diff] = dp[i][diff]
            for diff in dp[i]:
                if diff + rods[i] not in dp[i + 1]:
                    dp[i + 1][diff + rods[i]] = 0
                if abs(diff - rods[i]) not in dp[i + 1]:
                    dp[i + 1][abs(diff - rods[i])] = 0
                dp[i + 1][diff + rods[i]] = max(dp[i + 1][diff + rods[i]], dp[i][diff] + rods[i])
                dp[i + 1][abs(diff - rods[i])] = max(dp[i + 1][abs(diff - rods[i])], dp[i][diff], dp[i][diff] - diff + rods[i])
        if 0 in dp[-1]:
            return dp[-1][0]
        return 0
