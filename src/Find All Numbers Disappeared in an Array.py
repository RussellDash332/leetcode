class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [i + 1 for i in range(len(nums))]
        for i in nums:
            arr[i - 1] = 0
        return list(filter(lambda x: x, arr))
