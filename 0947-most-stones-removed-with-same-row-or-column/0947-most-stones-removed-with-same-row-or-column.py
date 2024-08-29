class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        visited = set()
        n = len(stones)
        connected_stones = [ [] for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    connected_stones[i].append(j)
                    connected_stones[j].append(i)
        
        
        def dfs(idx):
            if idx in visited:
                return
            visited.add(idx)
            for i in connected_stones[idx]:
                dfs(i)

        
        
        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt+=1
        return n-cnt