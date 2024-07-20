class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROW = len(rowSum)
        COL = len(colSum)
        ans = [[0]*COL for _ in range(ROW)]
        
        for r in range(ROW):
            for c in range(COL):
                curr_r = rowSum[r]
                curr_c = colSum[c]
                cell = min(curr_r, curr_c)
                ans[r][c]=cell
                rowSum[r]-=cell
                colSum[c]-=cell
        return ans
                
        