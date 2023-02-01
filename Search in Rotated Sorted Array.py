class Solution(object):
    def findMin(self, nums):
        if len(nums) <= 3:
            return nums.index(min(nums))
        l, r = 0, len(nums) - 1
        while l < (l + r) // 2 < r:
            m = (l + r) // 2
            if nums[l] < nums[m] and nums[m] > nums[r]: # m > l > r
                l = m
            elif nums[l] > nums[m] and nums[m] < nums[r]: # l > r > m
                r = m
            else:
                return l
        return min({nums[l]: l, nums[m]: m, nums[r]: r}.items())[1]

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 3:
            return nums.index(target) if target in nums else -1
        offset = self.findMin(nums)
        lo, hi, n = 0, len(nums)-1, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[(mid+offset)%n] == target:
                return (mid+offset)%n
            elif nums[(mid+offset)%n] > target:
                hi = max(mid - 1, 0)
            else:
                lo = min(mid + 1, len(nums)-1)
        if nums[(lo+offset)%n] == target:
            return (lo+offset)%n
        return -1
