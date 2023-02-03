class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            return max(nums)
        res = [0]*(len(nums)-1)
        res[0] = nums[0]
        for i in range(1, len(nums)-1):
            if i == 1: res[1] = nums[1]
            else: res[i] = max(res[i-2], res[i-3]) + nums[i]
        res2 = [0]*(len(nums)-1)
        res2[0] = nums[1]
        for i in range(2, len(nums)):
            if i == 2: res2[1] = nums[2]
            else: res2[i-1] = max(res2[i-3], res2[i-4]) + nums[i]
        return max(res[-3], res[-2], res[-1], res2[-3], res2[-2], res2[-1])
