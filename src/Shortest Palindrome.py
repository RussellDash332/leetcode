class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]: return s
        tmp = s+'?'+s[::-1]
        lps = [0]*len(tmp)
        for i in range(1, len(lps)):
            l = lps[i-1]
            while l > 0 and tmp[l] != tmp[i]:
                l = lps[l-1]
            if tmp[i] == tmp[l]: l += 1
            lps[i] = l
        return s[lps[-1]:][::-1] + s
