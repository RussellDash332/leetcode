class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dp = [0]*26
        for i in s:
            best = 0
            curr = ord(i)-97
            for p in range(26):
                if abs(p-curr) <= k: best = max(best, dp[p])
            dp[curr] = max(dp[curr], best+1)
        return max(dp)