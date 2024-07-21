class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        mat = [[0]*k for i in range(k)]
        
        def dfs(src, graph, visited, cur_path, res):
            if src in cur_path:
                return False
            if src in visited:
                return True
            
            visited.add(src)
            cur_path.add(src)
            
            for node in graph[src]:
                if not dfs(node, graph, visited, cur_path, res):
                    return False
            
            cur_path.remove(src)
            res.append(src)
            return True
        
        def top_sort(arr):
            hmap = defaultdict(list)
            LEN = len(arr)
            for i in arr:
                above = i[0]
                below = i[1]
                hmap[above].append(below)
            
            visited = set()
            cur_path = set()
            res = []
            
            for i in range(1, k+1):
                if not dfs(i, hmap, visited, cur_path, res):
                    return []
            return res[::-1]
        
        sorted_rows = top_sort(rowConditions)
        sorted_cols = top_sort(colConditions)
        if not sorted_rows or not sorted_cols:
            return []
        posi_dict = {i:[0,0] for i in range(1, k+1)}
        for idx, val in enumerate(sorted_rows):
            posi_dict[val][0] = idx
        for idx, val in enumerate(sorted_cols):
            posi_dict[val][1] = idx
        
        for i in range(1, k+1):
            r,c = posi_dict[i]
            mat[r][c] = i
        return mat
        
        
        
        
        
        
        
            