class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for k in range(len(nums)-2, -2, -1):
            if k == -1 or nums[k] < nums[k+1]: break
        if k == -1: return nums.reverse()
        for l in range(len(nums)-1, k-1, -1):
            if l == k or nums[l] > nums[k]: break
        nums[k], nums[l] = nums[l], nums[k]
        l, r = k+1, len(nums)-1
        while l < r: nums[l], nums[r], l, r = nums[r], nums[l], l+1, r-1
