class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        cnt = [0]*24
        for i in candidates:
            bits = bin(i)[2:]
            for idx, val in enumerate(reversed(bits)):
                cnt[idx]+= 1 if val=='1' else 0
        
        return max(cnt)