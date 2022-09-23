class Solution:
    def count_bits(self, num):
        count = 0
        while num:
            num>>=1
            count+=1
        return count
    def concatenatedBinary(self, n: int) -> int:
        out = 0
        mod = 10**9 + 7
        for val in range(n+1):
            out = ((out<<self.count_bits(val))+val)%mod
        return out
        