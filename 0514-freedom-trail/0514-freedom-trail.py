class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        RLEN = len(ring)
        def get_new_ind(start, end):
            # print ("in get ind", start, end)
            #right side
            if end>start:
                right = end-start
                left = start+ (RLEN-end)
                return min(right,left)
            else:
                # left side
                left = start-end
                right = RLEN-start+(end)
                return min(left, right)
        def dp(k, rind):
            if k>=len(key):
                return 0
            if (k,rind) in memo:
                return memo[(k,rind)]
            val = key[k]
            if ring[rind]==val:
                memo[(k, rind)] = dp(k+1, rind)+1
            else:
                local = float('inf')
                for i,j in enumerate(ring):
                    if j==val:
                        moves = get_new_ind(rind, i)+1
                        # print ('Move',moves, "KIND", k, "PASTRIND", rind, "new rind", i)
                        local = min(dp(k+1, i)+moves,local)
                memo[(k,rind)] = local
            return memo[(k,rind)]
        
        return dp(0, 0)
                        