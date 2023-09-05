class Solution:
    def bestClosingTime(self, customers: str) -> int:
        o = [0]; c = [0]
        for i in customers: o.append(o[-1]+(i=='N'))
        for i in customers[::-1]: c.append(c[-1]+(i=='Y'))
        return min((o[i]+c[len(c)-1-i], i) for i in range(len(o)))[1]
