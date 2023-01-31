class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1 and n not in s:
            r = 0
            s.add(n)
            while n:
                r += (n%10)**2
                n //= 10
            n = r
            print(n)
        return n == 1
