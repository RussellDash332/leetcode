class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        for i in range(len(mat)):
            mat[i] = [-1e12] + mat[i] + [-1e12]
        mat = [[-1e12]*len(mat[0])] + mat + [[-1e12]*len(mat[0])]
        def get_max(idx):
            return mat[idx].index(max(mat[idx]))
        def helper(lo, hi):
            if lo >= hi: return [lo, get_max(lo)]
            mid = (lo + hi) // 2
            mid2 = get_max(mid)
            if mat[mid-1][mid2] < mat[mid][mid2] > mat[mid+1][mid2]: return [mid, mid2]
            if mat[mid-1][mid2] < mat[mid][mid2]: return helper(mid+1, hi)
            return helper(lo, mid-1)
        r,c = helper(1, len(mat)-2)
        return [r-1,c-1]
