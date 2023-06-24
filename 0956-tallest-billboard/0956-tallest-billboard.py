class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {}
        n = len(rods)
        self.max_v = 0
        # Change it to sum
        
        # def dfs(set1, set2, ind):
        #     if ind==n:
        #         if sum(set1)==sum(set2):
        #             self.max_v = max(self.max_v, sum(set1))
        #             return
        #         return
        #     if (ind, set1, set2) in dp:
        #         return dp[(ind, set1, set2)]
        #     elif (ind, set2, set1) in dp:
        #         return dp[(ind, set2, set1)]
        #     val = rods[ind]
        #     v1=dfs(set1.union({val}), set2, ind+1)
        #     v2=dfs(set1, set2.union({val}), ind+1)
        #     v3 = dfs(set1, set2, ind+1)
        #     dp[(ind, set1, set2)]=max(v1,v2,v3)
        #     return
        # dfs(set(), set(), 0)
        # return self.max_v
        
        def dfs( diff, ind):
            if ind==n:
                print (diff, ind)
            if ind==n:
                if diff ==0:
                    # self.max_v = max(self.max_v, sum1)
                    return 0
                return -float('inf')
                
            if (ind, diff) in dp:
                return dp[(ind, diff)]
            val = rods[ind]
            v1 = val+dfs(diff+val ,ind+1)
            v2 = dfs(diff-val, ind+1)
            v3 = dfs(diff, ind+1)
            dp[(ind, diff)]=max(v1,v2,v3)
            return dp[(ind, diff)]
            return max(v1,v2,v3)
        return dfs(0, 0)

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            