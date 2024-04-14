class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.max = [i for i in range(N)]

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
                self.max[x] = max(self.max[x], self.max[y])
            else:
                self.p[x] = y
                self.max[y] = max(self.max[x], self.max[y])
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = min(max(0, max(nums)) + 1, 5*10**5)
        ufds = UFDS(k)
        got = [False]*(k)
        for i in nums:
            if 1 <= i <= k:
                got[i - 1] = True
                if i != 1 and got[i - 2]:
                    ufds.union(i - 1, i - 2)
                if i != k and got[i]:
                    ufds.union(i - 1, i)
        if not got[0]:
            return 1
        return ufds.max[ufds.find_set(0)] + 2
