class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0]*len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1: res[1] = nums[1]
            else: res[i] = max(res[i-2], res[i-3]) + nums[i]
        return max(res[-3:])
