class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bomb_dict = collections.defaultdict(set)
        total = len(bombs)
        for i in range(total-1):
            for j in range(i+1, total):
                b1 = bombs[i]
                b2 = bombs[j]
                x = (b2[0]-b1[0])**2
                y = (b2[1]-b1[1])**2
                dist = math.sqrt(x+y)
                if dist <=b1[2]:
                    bomb_dict[(b1[0],b1[1])].add((b2[0],b2[1]))
                if dist <=b2[2]:
                    bomb_dict[(b2[0],b2[1])].add((b1[0],b1[1]))
        max_v = 0

        count_dict = collections.defaultdict(int)
        
        for i in bombs:
            count_dict[(i[0],i[1])]+=1
        
        visited = set()

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            count = count_dict[node]
            for val in bomb_dict[node]:
                if val in bomb_dict:
                    count+=dfs(val)
                else:
                    if val not in visited:
                        visited.add(val)
                        count+=count_dict[node]
            return count
        # print (bomb_dict)
        for k in bomb_dict:
            
            out = dfs(k)

            visited = set()
            # print (k, out)
            max_v = max(out, max_v)
        
        return max_v if max_v >0 else 1