class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(numbers) - 1
        while numbers[lo] + numbers[hi] != target:
            if numbers[lo] + numbers[hi] > target:
                hi -= 1
            else:
                lo += 1
        return lo + 1, hi + 1
