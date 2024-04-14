class Solution(object):
    def merge(self, intervals):
        h=lambda a,b:0 if a[1]<b[0]or b[1]<a[0]else[min(a[0],b[0]),max(a[1],b[1])]
        return [r:=[],[[r.pop(),r.append(k)]if r and(k:=h(r[-1],j))else r.append(j)for j in sorted(intervals)]][0]

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        return self.merge(intervals + [newInterval])
