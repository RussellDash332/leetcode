class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        h = [[] for _ in range(numRows)]
        numRows -= 1; r = 0; z = 2*numRows
        for i in s:
            h[r].append(i); z -= 1
            if numRows <= z: r += 1
            else: r -= 1
            if z == 0: z = 2*numRows
        return ''.join(map(''.join, h))