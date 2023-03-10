class Solution(object):
    def findTheString(self, lcp):
        """
        :type lcp: List[List[int]]
        :rtype: str
        """
        res = [97]*len(lcp)
        for i in range(len(lcp)):
            if lcp[i][i] != len(lcp)-i: return ''
            for j in range(i+1, len(lcp)):
                if lcp[i][j] != lcp[j][i] or lcp[i][j] > len(lcp)-j: return ''
                if lcp[i][j] == 0 and res[i] == res[j]: res[j] += 1
                if res[j] > 122: return ''
        for i in range(len(lcp)-1):
            for j in range(i+1, len(lcp)-1):
                if res[i] == res[j] and lcp[i][j] != lcp[i+1][j+1] + 1: return ''
        for i in range(len(lcp)):
            for j in range(i+1, len(lcp)):
                if lcp[i][j] != 0 and res[i] != res[j]: return ''
        return ''.join(map(chr, res))
