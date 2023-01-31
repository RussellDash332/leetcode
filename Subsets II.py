class Solution(object):
    def subsets(self, nums, idx=0):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if idx == len(nums): return [[]]
        sub = self.subsets(nums, idx+1)
        return sub + [x + [nums[idx]] for x in sub]

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return {tuple(sorted(x)) for x in set(map(tuple, self.subsets(nums)))}
