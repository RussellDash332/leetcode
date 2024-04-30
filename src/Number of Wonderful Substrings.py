class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        H = [0]*1024; H[0] += 1
        p = A = 0
        K = (0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
        for i in word:
            p ^= 1<<(ord(i)-97)
            for j in K: A += H[j^p]
            H[p] += 1
        return A