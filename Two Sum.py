class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = []
            h[nums[i]].append(i)
        for i in h:
            if 2 * i == target:
                if len(h[i]) > 1:
                    return h[i][:2]
            elif target - i in h:
                return [h[i][0], h[target - i][0]]
