class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        n = ['']
        for i in s:
            if '0'<=i<='9': n[-1] += i
            elif n[-1]: n.append('')
        while not n[-1]: n.pop()
        n = [*map(int, n)]
        for i in range(len(n)-1):
            if n[i] >= n[i+1]: return False
        return True