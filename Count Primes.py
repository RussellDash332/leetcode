from bisect import bisect_left
class Solution:
    def countPrimes(self, n: int) -> int:
        spf = list(range(n+1))
        primes = []
        p = 2
        while p <= n:
            if spf[p] == p:
                primes.append(p)
                for i in range(p*p, n+1, p):
                    if spf[i] == i: spf[i] = p
            if p == 2: p -= 1
            p += 2
        return bisect_left(primes, n)
