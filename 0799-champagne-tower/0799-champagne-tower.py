class Solution:
    def champagneTower(self, poured: int, r: int, c: int) -> float:
        dp = {}
        def dfs(idx,col):
            if idx<0 or col<0:
                return 0
            if (idx,col) in dp:
                return dp[(idx,col)]
            if idx==col==0:
                if (idx,col)==(r,c):
                    return poured
                curr = poured-1
                return curr
            else:
                prev_r = idx-1
                prev_c = col
                if (idx,col)==(r,c):
                    return max(dfs(prev_r,prev_c-1)/2+dfs(prev_r,prev_c)/2,0)
                dp[(idx,col)] = max((dfs(prev_r,prev_c-1)/2+dfs(prev_r,prev_c)/2)-1,0)
                return dp[(idx,col)]
            
        out = max(min(dfs(r,c),1),0)
        # print (dp)
        return out