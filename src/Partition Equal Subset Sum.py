class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = {0}
        for i in nums:
            s |= {i+j for j in s}
        return sum(nums)%2==0 and sum(nums)//2 in s