class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        new_nums = nums[-k:] + nums[:-k]
        for _ in range(len(nums)): # no clear method
            nums.pop()
        nums.extend(new_nums)
