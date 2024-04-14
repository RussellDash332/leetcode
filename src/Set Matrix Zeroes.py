class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    r.add(i)
                    c.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in r or j in c:
                    matrix[i][j] = 0
