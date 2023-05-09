
from sys import stdin, stdout
class Solution:
    def BinaryInversions(self, n, bits):
        l, r = 0, n-1
        first, second, orig = bits[::], bits[::], bits[::]
        hasFirst, hasSecond = True, True
        
        for i in range(n):
            if hasFirst and bits[i] == 0:
                first[i] = 1
                hasFirst = False
            if hasSecond and bits[n-i-1] == 1:
                second[n-i-1] = 0
                hasSecond = False
        first_sum, second_sum, orig_sum = 0, 0, 0
        first_zeros, second_zeros, orig_zeros = 0, 0, 0
        for i in range(n-1, -1, -1):
            if first[i] == 0:
                orig_zeros += 1
            else:
                orig_sum += orig_zeros
            if second[i] == 0:
                second_zeros += 1
            else:
                second_sum += second_zeros
                
            if first[i] == 0:
                first_zeros += 1
            else:
                first_sum += first_zeros
        return max(orig_sum, first_sum, second_sum)

sol = Solution()
t = int(input())
for _ in range(t):
    n = int(input())
    bits = list(map(int, input().split()))
    print(sol.BinaryInversions(n, bits))

    