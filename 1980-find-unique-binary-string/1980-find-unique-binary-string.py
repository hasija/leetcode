class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        uniq_set = set(nums)
        n = len(nums)
        for i in range(2**n):
            binary = bin(i)[2:]
            final_b = '0'*(n-len(binary))+binary
            if final_b not in uniq_set:
                return final_b
            