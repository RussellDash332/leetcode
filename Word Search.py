class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        path = []
        visited = set()
        got = [False]
        word2 = list(word)
        def dfs(r, c):
            if got[0]: return
            path.append(board[r][c])
            if board[r][c] != word2[len(path)-1]:
                return path.pop()
            if path == word2:
                got[0] = True
                return
            visited.add((r, c))
            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                if 0 <= r+dr < len(board) and 0 <= c+dc < len(board[0]) and (r+dr, c+dc) not in visited:
                    dfs(r+dr, c+dc)
            path.pop()
            visited.remove((r,c))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i, j)
        return got[0]
