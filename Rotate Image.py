class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new = [[matrix[-j-1][i] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        matrix.clear()
        matrix.extend(new)
