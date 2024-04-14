class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        def helper(target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        l, r = min(helper(target), len(nums) - 1), max(helper(target + 1) - 1, 0)
        if nums[l] != target:
            l = -1
        if nums[r] != target:
            r = -1
        return [l, r]
