class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        def can(x):
            l, r = 0, 1
            s = 0
            while r < len(nums):
                while nums[r]-nums[l] > x: l += 1
                s += r-l
                r += 1
            return s
        lo, hi = 0, nums[-1]
        while lo < hi:
            mi = (lo+hi)//2
            if can(mi) >= k: hi = mi
            else: lo = mi+1
        return lo