class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = [0]*2002
        for i in nums: h[i] = 1
        for i in range(1000, 0, -1):
            if h[i] and h[-i]: return i
        return -1