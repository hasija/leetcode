class Solution:
    def findKthNumber(self, n, k):
        curr = 1
        
        def cal_steps(curr):
            steps = 0
            nxt = curr+1
            while curr<=n:
                steps += min(n+1, nxt)-curr
                nxt*=10
                curr*=10
            return steps
        k-=1
        while k>0:
            steps = cal_steps(curr)
            if steps>k:
                curr*=10
                k-=1
            else:
                k-=steps
                curr+=1

        return curr
                    
                
                