class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*len(s)
        dp[0] = int(0 < int(s[0]) < 27)
        if s == s[0]: return dp[0]
        dp[1] = dp[0] * (0 < int(s[1]) < 27) + (0 < int(s[:2]) < 27 and s[0] != '0')
        for i in range(2, len(s)):
            dp[i] = dp[i-1] * (0 < int(s[i]) < 27) + dp[i-2] * (0 < int(s[i-1:i+1]) < 27 and s[i-1] != '0')
        return dp[-1]
