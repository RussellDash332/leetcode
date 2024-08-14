class Solution(object):
    from bisect import bisect_left, bisect_right
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = bisect_right([a[0] for a in matrix], target)-1
        c = bisect_left(matrix[r], target)
        if c == len(matrix[0]): return False
        return matrix[r][c] == target