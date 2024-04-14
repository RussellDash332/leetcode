class Solution(object):
    def subsets(self, nums, idx=0):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if idx == len(nums): return [[]]
        sub = self.subsets(nums, idx+1)
        return sub + [x + [nums[idx]] for x in sub]
