class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target: return True
            target = self.rotate(target)
        return False

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        return [[matrix[-j-1][i] for j in range(len(matrix[0]))] for i in range(len(matrix))]
