class Solution:
    def numberOfWays(self, cor: str) -> int:
        ways = []
        curr = 0
        start = 0
        for ind,i in enumerate(cor):
            if i=='S':
                if curr==2:
                    ways.append(ind-start)
                    curr=1
                else:
                    curr+=1
                if curr==2:
                    start = ind
        
        if curr!=2:
            return 0
        ans = 1
        for i in ways:
            ans*=i
        return ans%((10**9)+7)
                
                