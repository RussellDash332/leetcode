class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        t = []; m = {}; a = []
        for p, h, d in sorted(zip(positions, healths, directions)):
            if not t or t[-1][2] == d: t.append([p, h, d])
            else:
                while t and h and t[-1][2] == 'R' and d == 'L':
                    if t[-1][1] == h: t.pop(); h = 0
                    elif t[-1][1] < h: t.pop(); h -= 1
                    else: t[-1][1] -= 1; h = 0
                if h: t.append([p, h, d])
        for p, h, _ in t: m[p] = h
        for i in positions:
            if i in m: a.append(m[i])
        return a