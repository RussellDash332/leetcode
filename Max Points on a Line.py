class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        best, t = 1, len(points)
        h, v = {}, {}
        for i in range(t-1):
            x1, y1 = points[i]
            h = {}
            for j in range(i+1, t):
                x2, y2 = points[j]
                a, b = y2 - y1, x2 - x1
                d = gcd(a, b); a//=d; b//=d
                if b == 0 and a < 0: a, b = -a, -b
                tup = (a, b)
                if tup not in h: h[tup] = 1
                h[tup] += 1
            best = max(best, max(h.values()) if h else 1)
        return best
