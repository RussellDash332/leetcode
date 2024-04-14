class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        h=lambda a,b:0 if a[1]<b[0]or b[1]<a[0]else[min(a[0],b[0]),max(a[1],b[1])]
        return [r:=[],[[r.pop(),r.append(k)]if r and(k:=h(r[-1],j))else r.append(j)for j in sorted(intervals)]][0]
