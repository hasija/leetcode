class Solution:
    def validArrangement(self, pairs):
        graph = defaultdict(list)
        inbound = defaultdict(int)
        outbound = defaultdict(int)
        all_pairs = set()
        for i,j in pairs:
            outbound[i]+=1
            inbound[j]+=1
            graph[i].append(j)
            all_pairs.add(i)
            all_pairs.add(j)
        # print("graph", graph)
        start = -1
        for i in all_pairs:
            if inbound[i]==outbound[i]-1:
                start = i
                break
        
        if start ==-1:
            start = pairs[0][0]
        
        # print("start node", start)
        res = []
        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
            res.append(node)
        
        dfs(start)
        
        # print(res)
        res = res[::-1]
        # print(res)
        ans = []
        for i in range(1, len(res)):
            ans.append([res[i-1],res[i]])
        return ans