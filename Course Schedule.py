class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        vis = set()
        cyc = [False]
        mem = set()
        def trav(p):
            if p in mem: return
            if cyc[0]: return
            if p in vis:
                cyc[0] = True
                return
            vis.add(p)
            if p in g:
                for i in g[p]:
                    trav(i)
            vis.remove(p)
            mem.add(p)
        
        g = {}
        for a, b in prerequisites:
            if a not in g: g[a] = []
            g[a].append(b)
        
        for i in g:
            vis.clear()
            trav(i)
        return not cyc[0]
