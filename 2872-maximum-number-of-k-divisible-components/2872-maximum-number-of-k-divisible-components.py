class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        def dfs(curr, parent):
            # print("dfs for node", curr)
            sum_ = 0
            for node in graph[curr]:
                if node!=parent:
                    sum_+=dfs(node, curr)
            sum_+=values[curr]
            sum_%=k
            if sum_==0:
                self.ans+=1
            # print("sum val", sum_)
            return sum_
        
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        self.ans = 0
        dfs(0, -1)
        return self.ans
        
            
            