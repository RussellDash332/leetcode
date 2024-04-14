class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        r, c = 0, 0
        dr, dc = 0, 1
        done = set()
        el = 1
        while el <= n**2:
            while 0 <= r < n and 0 <= c < n and (r, c) not in done:
                done.add((r, c))
                matrix[r][c] = el
                el += 1
                r, c = r+dr, c+dc
            r, c = r-dr, c-dc
            dr, dc = dc, -dr
            r, c = r+dr, c+dc
        return matrix
