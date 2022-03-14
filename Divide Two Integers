class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # I have to >:)
        if dividend * divisor < 0:
            return max(-(abs(dividend) // abs(divisor)), -2**31)
        return min(dividend // divisor, 2**31 - 1)
