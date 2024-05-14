class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        k = ((0, -1), (0, 1), (1, 0), (-1, 0))
        def bt(r, c):
            if not (len(grid)>r>-1<c<len(grid[0])) or grid[r][c] == 0: return 0
            old = grid[r][c]
            grid[r][c] = ans = 0
            for dr, dc in k: ans = max(ans, bt(r+dr, c+dc))
            grid[r][c] = old
            return ans+old
        return max(bt(i, j) for i in range(len(grid)) for j in range(len(grid[0])))