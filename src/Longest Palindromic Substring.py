class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]: return s
        dp = [['']*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i != 0:
                dp[i][i-1] = dp[i-1][i] = (s[i] == s[i-1])
        for i in range(len(s)-1,-1,-1):
            for j in range(i+2, len(s)):
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        best = (1000, 0)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j]:
                    best = max([best, (i, j)], key=lambda x: x[1]-x[0])
        l, r = best
        return s[l:r+1]
