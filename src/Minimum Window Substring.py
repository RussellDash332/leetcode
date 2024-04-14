class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        h, st, r = {}, 0, {}
        for i in t:
            if i not in r: r[i] = 0
            r[i] += 1
            h[i] = 0
        best = (1e9, 0, 0)
        good = 0
        while st < len(s) and s[st] not in r: st += 1
        if st == len(s): return ''
        for e in range(st, len(s)):
            if s[e] in r:
                if s[e] not in h: h[s[e]] = 0
                h[s[e]] += 1
                if h[s[e]] == r[s[e]]: good += 1
                while good == len(r):
                    best = min(best, (e-st, e, st))
                    h[s[st]] -= 1
                    if h[s[st]] < r[s[st]]: good -= 1
                    st += 1
                    while st < len(s) and s[st] not in r:
                        st += 1
        if best[0] == 1e9: return ''
        return s[best[2]:best[1]+1]
