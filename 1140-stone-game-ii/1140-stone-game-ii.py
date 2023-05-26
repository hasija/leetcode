class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        
        def dp(p, i, m):
            if i >=len(piles):
                return 0
            
            if (p,i,m) in memo:
                return memo[(p,i,m)]
            val = float('inf') if p else -float('inf')
            val_arr = []
            for x in range(1, 2*m+1):
                
                if p:
                    curr = dp(not p, i+x, max(m, x))
                    val = min(val, curr)
                else:
                    curr = sum(piles[i:i+x])+dp(not p, i+x, max(m, x))
                    val = max(val, curr)
                # val_arr.append(curr)
            # print ("value at i ,p ",i,p, val_arr)
            memo[(p,i,m)] = val
            return val
            # return min(val_arr) if p else max(val_arr)
        return dp(False, 0, 1)
                    
                
            