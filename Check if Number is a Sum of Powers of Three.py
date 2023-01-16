class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        arr = []
        while n:
            arr.append(n % 3)
            n //= 3
        return 2 not in arr
