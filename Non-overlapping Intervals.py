class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        res = []
        for itv in sorted(intervals, key=lambda x:x[::-1]):
            s, e = itv
            if not res or s >= res[-1][1]:
                res.append(itv)
        return len(intervals) - len(res)
