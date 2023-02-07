class Trie(object):

    def __init__(self):
        self.t = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        ptr = self.t
        for i in word + '.':
            if i not in ptr:
                ptr[i] = {}
            ptr = ptr[i]

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(r, c, ptr, path):
            tmp = board[r][c]
            path.append(tmp)
            if '.' in ptr:
                del ptr['.']
                res.add(''.join(path))
            board[r][c] = '?'
            for dr, dc in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if board[nr][nc] in ptr:
                        dfs(nr, nc, ptr[board[nr][nc]], path)
            path.pop()
            board[r][c] = tmp
        
        trie, res = Trie(), set()
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.t:
                    dfs(i, j, trie.t[board[i][j]], [])
        return res
