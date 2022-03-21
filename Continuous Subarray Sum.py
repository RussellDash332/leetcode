class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d, p = {0: -1}, 0
        for i in range(len(nums)):
            p += nums[i]
            p %= k
            if p in d:
                if i - d[p] >= 2:
                    return True
            else:
                d[p] = i
        return False
