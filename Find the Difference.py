class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for l in s:
            if l not in d:
                d[l] = 0
            d[l] += 1
        for l in t:
            if l not in d:
                return l
            d[l] -= 1
            if d[l] == 0:
                del d[l]
        return list(d.keys())[0]
