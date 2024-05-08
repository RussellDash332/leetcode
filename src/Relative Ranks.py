class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        r = sorted((-score[i], i) for i in range(len(score)))
        a = [-1]*len(score)
        a[r[0][1]] = 'Gold Medal'
        if len(score) > 1: a[r[1][1]] = 'Silver Medal'
        if len(score) > 2: a[r[2][1]] = 'Bronze Medal'
        for i in range(3, len(score)):
            a[r[i][1]] = str(i+1)
        return a