class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for i in tokens:
            if i in '+-*/':
                b, a = s.pop(), s.pop()
                if i == '+': s.append(a+b)
                elif i == '-': s.append(a-b)
                elif i == '*': s.append(a*b)
                elif a*b >= 0: s.append(a//b)
                else: s.append(-(-a//b))
            else:
                s.append(int(i))
        return int(s[0])