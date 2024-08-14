class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1; s = 0
        ml, mr = height[l], height[r]
        while l < r:
            if ml < mr:
                l += 1
                ml = max(ml, height[l])
                s += ml-height[l]
            else:
                r -= 1
                mr = max(mr, height[r])
                s += mr-height[r]
        return s