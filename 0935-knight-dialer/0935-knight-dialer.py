class Solution:
    def knightDialer(self, n: int) -> int:
        j_map = {0:[4,6],
                 1:[8,6],
                 2:[7,9],
                 3:[8,4],
                 4:[3,9,0],
                 6:[1,7,0],
                 7:[2,6],
                 8:[1,3],
                 9:[4,2],5:[]
                }
        mod = (10**9)+7
        ans = 0
        dp = {}
        def dfs(k,jump):
            out = 0
            if (k,jump) in dp:
                return dp[(k,jump)]
            if jump==0:
                return 1
            for nxt in j_map[k]:
                out+=dfs(nxt,jump-1)
            out%=mod
            dp[(k,jump)]=out
            return out
        
        
        for k,v in j_map.items():
            ans+=dfs(k,n-1)
            ans%=mod
        return ans