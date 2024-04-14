class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p, n, b = 1, 1, nums[0]
        for i in nums:
            p, n = max(i, max(p*i, n*i)), min(i, min(p*i, n*i))
            b = max(b, p, n)
        return b
