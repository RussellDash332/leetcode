class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = []; sgn = 0
        for i in s:
            if sgn == 0 and i == ' ': continue
            elif sgn == 0 and (i == '-' or i == '+'): ss.append(i); sgn = 1
            elif '0' <= i <= '9': ss.append(i); sgn = 1
            else: break
        ss = ''.join(ss)
        try:
            return min(max(int(ss), -2**31), 2**31-1)
        except:
            return 0