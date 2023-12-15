class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = paths[0][0]
        h_map = defaultdict(list)
        for i,j in paths:
            h_map[i].append(j)
        
        while h_map[start]:
            start = h_map[start][0]
        return start
            
            