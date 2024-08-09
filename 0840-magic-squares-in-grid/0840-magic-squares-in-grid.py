class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        
        
        def check_sq(r,c):
            seen = set()
            row_sum = [0,0,0]
            col_sum = [0,0,0]
            dia_left = 0
            dia_right = 0
            for i in range(3):
                for j in range(3):
                    row = r+i
                    col = c+j
                    curr = grid[row][col]
                    if i==j:
                        dia_left+=curr
                    if 2-j==i:
                        dia_right+=curr
                    if curr>9 or curr<=0:
                        return False
                    if curr in seen:
                        return False
                    seen.add(curr)
                    row_sum[i]+=curr
                    col_sum[j]+=curr
            if  (all([True for r in row_sum if row_sum[0]==r]) and
                all([True for r in col_sum if col_sum[0]==r]) and
                row_sum[0]==col_sum[0] and dia_left == dia_right == col_sum[0]):
                    return True
            return False
            
                
                    
        
        
        for r in range(rows-2):
            for c in range(cols-2):
                if check_sq(r,c):
                    ans+=1
        
        return ans