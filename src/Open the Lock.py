class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        g = [[] for _ in range(10000)]
        v = [0]*10001
        d = set(map(int, deadends))
        for i in range(10000):
            if i in d: continue
            k = list(str(i).zfill(4))
            for j in range(4):
                k[j] = chr((ord(k[j])-47)%10+48)
                g[i].append(int(''.join(k)))
                k[j] = chr((ord(k[j])-49)%10+48)
            for j in range(4):
                k[j] = chr((ord(k[j])-49)%10+48)
                g[i].append(int(''.join(k)))
                k[j] = chr((ord(k[j])-47)%10+48)
        q = [(0, -1)]
        for u, p in q:
            if v[u]: continue
            v[u] = v[p]+1
            for w in g[u]: q.append((w, u))
        return v[int(target)]-1