class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for p in s:
            if not stack or p in match:
                stack.append(p)
            elif stack[-1] in match and match[stack[-1]] == p:
                stack.pop()
            else:
                return False
        return not stack
