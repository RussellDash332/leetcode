class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Not optimal but works
        return list(filter(lambda x: nums.count(x) != 2, nums))
