from heapq import *
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = [-x for x in nums]
        heapify(nums)
        heapify(nums2)
        a, b, c, d, e, f = heappop(nums), heappop(nums), heappop(nums), heappop(nums2), heappop(nums2), heappop(nums2)
        return max(a*b*-d, -d*e*f)
