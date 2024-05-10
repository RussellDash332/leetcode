class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        p = [(float(arr[i])/arr[j], arr[i], arr[j]) for i in range(len(arr)) for j in range(i+1, len(arr))]
        p.sort(); return [p[k-1][1], p[k-1][2]]