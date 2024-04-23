class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
            

        if n<=2:
            return [i for i in range(n)]
        
        leafs = []
        for i,j in graph.items():
            if len(j)==1:
                leafs.append(i)
        
        while n>2:
            new_leafs = set()
            for leaf in leafs:
                node = graph[leaf].pop()
                graph.pop(leaf)
                graph[node].remove(leaf)
                if len(graph[node])==1:
                    new_leafs.add(node)
                n-=1
            if new_leafs:
                leafs = new_leafs
        return [i for i,j in graph.items()]
                
                