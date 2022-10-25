class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        i = 0
        h = {}
        for j, l in enumerate(s):
            if l in h:
                i = max(h[l] + 1, i)
            h[l] = j
            m = max(m, j - i + 1)
        return m
