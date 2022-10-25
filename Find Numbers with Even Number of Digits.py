class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(list(filter(lambda x: len(str(x)) % 2 == 0, nums)))
