import heapq
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        grid = [[0]*n for x in range(k+1)]
        if k<1 or len(prices)<2:
            return 0
        local_max = [[0]*n for x in range(k+1)]
        for row in range(0, k+1):
            for col in range(n):
                if row==0:
                    if col==0:
                        local_max[row][col]=-prices[col]
                    else:
                        local_max[row][col] =max(0-prices[col], local_max[row][col-1])
                    continue
                if col==0:
                    local_max[row][col]=-prices[col]
                    continue
                profit_curr = max(grid[row][col-1], 
                                 (prices[col]+local_max[row-1][col-1])
                                 )
                grid[row][col]=profit_curr
                local_max[row][col]=max(profit_curr-prices[col], local_max[row][col-1])
        # print (local_max,'local max')
        # print (grid,'global max')
        return grid[k][-1]
                
            
            
            
            
            