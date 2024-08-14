class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        z = [0]*len(temperatures); s = []
        for i in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[i]:
                m = s.pop()
                z[m] = i-m
            s.append(i)
        return z