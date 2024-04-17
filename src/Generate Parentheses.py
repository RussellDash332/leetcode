class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []; ans = []
        def helper(op, cl):
            if op == cl == n:
                return ans.append(''.join(s))
            if op < n:
                s.append('(')
                helper(op+1, cl)
                s.pop()
            if cl < op:
                s.append(')')
                helper(op, cl+1)
                s.pop()
        helper(0, 0)
        return ans