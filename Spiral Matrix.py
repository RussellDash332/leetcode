class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        R, C = len(matrix), len(matrix[0])
        N = R*C
        r, c = 0, 0
        dr, dc = 0, 1
        res = []
        done = set()
        while len(res) != N:
            while 0 <= r < R and 0 <= c < C and (r, c) not in done:
                done.add((r, c))
                res.append(matrix[r][c])
                r, c = r+dr, c+dc
            r, c = r-dr, c-dc
            dr, dc = dc, -dr
            r, c = r+dr, c+dc
        return res
