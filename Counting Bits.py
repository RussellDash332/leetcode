class Solution:
    def countBits(self, n: int) -> List[int]:
        bits, result, ones = [0], [0], 0
        for _ in range(n):
            bits[0] += 1
            ones += 1
            for i in range(len(bits)-1):
                if bits[i] == 1:
                    break
                else:
                    bits[i] = 0
                    bits[i+1] += 1
                    ones -= 1
            if bits[-1] == 2:
                bits[-1] = 0
                bits.append(1)
                ones -= 1
            result.append(ones)
        return result
