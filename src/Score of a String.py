class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a)-ord(b)) for a, b in zip(s, s[1:]))