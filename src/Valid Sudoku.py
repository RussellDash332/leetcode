class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            r = []; c = []; s = []
            for j in range(9):
                if board[i][j] != '.': r.append(board[i][j])
                if board[j][i] != '.': c.append(board[j][i])
                if board[3*(i//3)+j//3][3*(i%3)+j%3] != '.': s.append(board[3*(i//3)+j//3][3*(i%3)+j%3])
            if len(set(r)) != len(r): return False
            if len(set(c)) != len(c): return False
            if len(set(s)) != len(s): return False
        return True