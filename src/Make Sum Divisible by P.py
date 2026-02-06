class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        P = [s:=0] + [s:=s+i for i in nums]
        S = P[-1]%p
        H = {}
        Z = []
        for i in range(len(nums)+1):
            k = P[i]%p
            if k not in H: H[k] = []
            H[k].append(i)
        for m in H:
            a = H[m]; b = H.get((m+S)%p, []); r = 0
            for l in range(len(a)):
                while r < len(b) and b[r] < a[l]: r += 1
                if r < len(b): Z.append(b[r]-a[l])
        return min([z for z in Z if z < len(nums)], default=-1)