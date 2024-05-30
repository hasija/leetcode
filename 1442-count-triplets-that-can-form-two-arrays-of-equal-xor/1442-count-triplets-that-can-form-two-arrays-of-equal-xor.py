class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        LEN = len(arr)+1
        cnt = 0
        prefix_xor = [0]+arr.copy()
        for i in range(1, LEN):
            prefix_xor[i] ^= prefix_xor[i-1] 
        for start in range(LEN-1):
            s_xor = prefix_xor[start]
            for end in range(start+1, LEN):
                e_xor = prefix_xor[end]
                if s_xor==e_xor:
                    cnt+= (end-start-1)
        return cnt
            