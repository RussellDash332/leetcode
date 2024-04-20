class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        vis = [[0]*len(land[0]) for _ in range(len(land))]
        for i in range(len(land)):
            for j in range(len(land[0])):
                if vis[i][j] or not land[i][j]: continue
                sa, sb = i, j; sc = sd = 0
                q = [(i, j)]
                for r, c in q:
                    if vis[r][c]: continue
                    vis[r][c] = 1; sc, sd = max((sc, sd), (r, c))
                    for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                        if len(land)>r+dr>-1<c+dc<len(land[0]) and land[r+dr][c+dc]: q.append((r+dr, c+dc))
                ans.append([sa, sb, sc, sd])
        return ans