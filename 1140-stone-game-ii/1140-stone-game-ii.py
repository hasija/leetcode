class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}
        def dp(turn, m, idx):
            if idx>=n:
                return 0
            
            if (turn, m, idx) in memo:
                return memo[(turn, m, idx)]
            local_max = 0
            local_min = float('inf')
            cnt = 0
            for i in range(0, (m*2)):
                if idx+i>=n:
                    break
                cnt+=piles[idx+i]
                new_m = max(m,i+1)
                
                if turn == 'alice':
                    resp = dp('bob', new_m, (idx+i+1))
                    local_max = max(resp+cnt,local_max)
                    # print ("Turn ALICE", 'local-max',local_max, 'loop idx',i, 'dflt idx',idx)
                else:
                    resp = dp('alice', new_m, (idx+i+1))
                    local_min = min(resp,local_min)
            
            
            if turn == 'alice':
                memo[(turn, m, idx)]=local_max
                return local_max
            else:
                memo[(turn, m, idx)]=local_min
                return local_min
        return dp('alice', 1, 0)