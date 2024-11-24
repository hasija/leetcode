class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_cnt = 0
        min_val = float('inf')
        ans = 0
        is_zero_present = False
        for r in matrix:
            for val in r:
                if val<0:
                    neg_cnt+=1
                if val == 0:
                    is_zero_present = True
                min_val = min(min_val, abs(val))
                ans+=abs(val)
        
        if neg_cnt%2==0 or is_zero_present:
            return ans
        else:
            return ans-(2*min_val)
        