class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ans = [0]*n
        g = [[] for _ in range(n)]
        d = [0]*n
        par = list(range(n))
        sx = [0]*n
        s = [(0, 0)]
        tf = n
        for a, b in edges:
            g[a].append(b); g[b].append(a)
        while s:
            ub, p = s.pop(); u = ub//2
            if ub%2:
                par[u] = p
                for t in g[u]:
                    if t != p:
                        sx[u] += sx[t]
                sx[u] += 1
            else:
                s.append((ub+1, p))
                for t in g[u]:
                    if t != p:
                        d[t] = d[u]+1
                        s.append((2*t, u))
        s = [(0, 0, sum(d))]
        while s:
            u, p, dd = s.pop()
            ans[u] = dd
            for t in g[u]:
                if t != p:
                    s.append((t, u, dd+tf-2*sx[t]))
        return ans