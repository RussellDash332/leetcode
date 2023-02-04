class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [['']*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i != 0:
                dp[i][i-1] = dp[i-1][i] = (s[i] == s[i-1])
        for i in range(len(s)-1,-1,-1):
            for j in range(i+2, len(s)):
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        cnt = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                cnt += dp[i][j]
        return cnt
