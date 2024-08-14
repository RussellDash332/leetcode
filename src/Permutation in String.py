class Solution(object):
    from collections import Counter
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1): return False
        c = Counter()
        for i in range(len(s1)):
            c[s1[i]] -= 1
            c[s2[i]] += 1
        m = sum(1 for i in c.values() if i)
        if m == 0: return True
        for i in range(len(s1), len(s2)):
            if c[s2[i]] == 0: m += 1
            c[s2[i]] += 1
            if c[s2[i]] == 0: m -= 1
            if c[s2[i-len(s1)]] == 0: m += 1
            c[s2[i-len(s1)]] -= 1
            if c[s2[i-len(s1)]] == 0: m -= 1
            if m == 0: return True
        return False