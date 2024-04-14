class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([x for x in s if x.isalnum()]).lower()
        return s == s[::-1]
