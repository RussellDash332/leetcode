class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        pos = (m + n + 1) // 2
        start, end = 0, m
        while start <= end:
            mid = (start + end) // 2
            left1, left2 = mid, pos - mid
            l1 = nums1[left1 - 1] if left1 else -1e9
            l2 = nums2[left2 - 1] if left2 else -1e9
            r1 = nums1[left1] if left1 < m else 1e9
            r2 = nums2[left2] if left2 < n else 1e9
            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                return max(l1, l2)
            elif l1 > r2:
                end = mid - 1
            else:
                start = mid + 1
