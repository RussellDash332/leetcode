class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        result = []
        nums3 = nums1[:m]
        while nums3 and nums2:
            if nums3[0] < nums2[0]:
                result.append(nums3.pop(0))
            else:
                result.append(nums2.pop(0))
        result.extend(nums3)
        result.extend(nums2)
        while nums1:
            nums1.pop()
        for i in result:
            nums1.append(i)
