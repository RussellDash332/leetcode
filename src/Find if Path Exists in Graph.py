class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        al = [[] for _ in range(n)]
        for a, b in edges: al[a].append(b); al[b].append(a)
        v = [0]*n
        s = [source]
        while s:
            u = s.pop()
            if v[u]: continue
            v[u] = 1; s.extend(al[u])
        return v[destination]