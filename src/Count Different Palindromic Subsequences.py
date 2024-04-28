class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)): dp[i][i] = 1
        for k in range(2, len(s)+1):
            for i in range(len(s)-k+1):
                j = i+k-1
                if s[i] == s[j]:
                    l = i+1; r = j-1
                    dp[i][j] = 2*dp[i+1][j-1]
                    while l <= r and s[l] != s[i]: l += 1
                    while l <= r and s[r] != s[i]: r -= 1
                    if l < r: dp[i][j] -= dp[l+1][r-1]
                    elif l == r: dp[i][j] += 1
                    else: dp[i][j] += 2
                else: dp[i][j] = dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
                dp[i][j] %= 10**9+7
        return dp[0][-1]