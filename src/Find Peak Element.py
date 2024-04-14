class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-1e12] + nums + [-1e12]
        def helper(lo, hi):
            if lo >= hi: return lo
            mid = (lo + hi) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]: return mid
            if nums[mid-1] < nums[mid]: return helper(mid+1, hi)
            return helper(lo, mid-1)
        return helper(1, len(nums)-2)-1
