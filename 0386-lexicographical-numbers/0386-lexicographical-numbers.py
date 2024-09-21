class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.out = []
        def dfs(past):
            self.out.append(int(past))
            for i in range(10):
                curr = past+str(i)
                if int(curr)<=n:
                    dfs(curr)
                else:
                    break
        for i in range(1,10):
            if i<=n:
                dfs(str(i))
            else:
                break
        
        return self.out
                
                
            
            