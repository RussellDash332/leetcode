class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        xors = []
        v = 0
        for i in arr:
            v ^= i
            xors.append(v)
        print(xors)
        return [xors[j] ^ xors[i - 1] if i != 0 else xors[j] for i, j in queries]
