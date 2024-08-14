from collections import *
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = Counter(tasks).values()
        m = max(c)
        return max(len(tasks), (m-1)*(n+1)+sum(i==m for i in c))