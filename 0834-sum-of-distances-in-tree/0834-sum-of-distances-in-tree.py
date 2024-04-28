class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph  = defaultdict(set)
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        count = defaultdict(int)
        res = defaultdict(int)
        def dfs(node, past):
            count[node]+=1
            res[node] = 0
            for i in graph[node]:
                if i==past:
                    continue
                count[node]+=dfs(i, node)
                res[node] += res[i]+count[i]
            return count[node]
        dfs(0, None)
        
        def dfs2(node, past):
            if past is not None:

                left_side = (res[past]-res[node]-count[node])
                left_moves = n-count[node]
                res[node] += left_side+left_moves
            for i in graph[node]:
                if i == past:
                    continue
                dfs2(i, node)
            # print ('node',node,"new res", res)
        
        dfs2(0, None)
        # print (res)
        # print (count, res)
        ans = [0]*n
        for i, j in res.items():
            ans[i]=j
        return ans