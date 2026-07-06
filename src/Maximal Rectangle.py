class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        Z=0;S=len(matrix[0]);H=[Z]*-~S
        for r in matrix:
            for c in range(S):H[c]=-~H[c]*int(r[c])
            s=[]
            for i in range(-~S):
                while s and H[s[-1]]>H[i]:Z=max(Z,H[s.pop()]*(i-s[-1]-1if s else i))
                s+=[i]
        return Z