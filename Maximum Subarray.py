class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane?
        best, curr = -1e9, 0
        for i in nums:
            curr += i
            best, curr = max(best, curr), max(curr, 0)
        return best
