class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ROW = len(matrix)
        COL = len(matrix[0])
        ans = []
        for r in range(ROW):
            curr_min = min(matrix[r])
            col = matrix[r].index(curr_min)
            curr_max = -float('inf')
            for c in range(ROW):
                curr_max = max(matrix[c][col], curr_max)
            if curr_max==curr_min:
                ans.append(curr_max)
            
            
        return ans