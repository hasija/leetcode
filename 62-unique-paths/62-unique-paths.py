class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        run_arr = [[0]*n for x in range(m)]
        
        for row in range(m):
            for col in range(n):
                cell = run_arr[row][col]
                count = 0
                if row==0 and col ==0:
                    run_arr[row][col]=1
                    continue
                if row==0 and col>0:
                    run_arr[row][col]=1
                    continue
                if col==0 and row>0:
                    run_arr[row][col]=1
                    continue
                if row-1>=0:
                    count+=run_arr[row-1][col]
                if col-1>=0:
                    count+=run_arr[row][col-1]
                run_arr[row][col]=count
                
        # print (run_arr)
       
        return run_arr[m-1][n-1]
                    
        