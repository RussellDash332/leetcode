class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[:1:-1]
        return int(b + '0'*(32-len(b)), 2)
