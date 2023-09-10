class Solution:
    def countOrders(self, n: int) -> int:
        mod = (10**9)+7
        past = 1
        for i in range(1,n+1):
            new = ((i*2)-1)*i
            past = past*new
            past = past%mod
            # print (i,past)
        
        return past
            
            
        