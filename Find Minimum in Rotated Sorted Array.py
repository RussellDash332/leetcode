class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            return min(nums)
        l, r = 0, len(nums) - 1
        while l < (l + r) // 2 < r:
            m = (l + r) // 2
            if nums[l] < nums[m] and nums[m] > nums[r]: # m > l > r
                l = m
            elif nums[l] > nums[m] and nums[m] < nums[r]: # l > r > m
                r = m
            else:
                return nums[l]
        return min(nums[l], nums[m], nums[r])
