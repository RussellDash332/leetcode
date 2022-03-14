class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Not optimal but works
        # return list(filter(lambda x: nums.count(x) != 2, nums))
        
        xor = 0
        for i in nums:
            xor ^= i
        
        xor &= -xor
        a, b = 0, 0
        for i in nums:
            if xor & i:
                a ^= i
            else:
                b ^= i
        return a, b
