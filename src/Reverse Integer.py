class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0
        x = abs(x)
        rev = 0
        
        while x > 0:
            rev *= 10
            rev += x % 10
            x //= 10
        
        if -2**31 <= rev <= 2**31 - 1:
            if is_negative:
                return -rev
            return rev
        return 0
