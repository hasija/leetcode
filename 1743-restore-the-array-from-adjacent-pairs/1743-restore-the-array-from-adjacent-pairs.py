class Solution:
    def restoreArray(self, pair: List[List[int]]) -> List[int]:
        dag = collections.defaultdict(set)
        for i,j in pair:
            dag[i].add(j)
            dag[j].add(i)
        
        for k,v in dag.items():
            if len(v)==1:
                break
        start = k
        ans = [k]
        visited = set([k])
        while len(ans)<=len(pair):
            vals = dag[k]
            for v in vals:
                if v in visited:
                    continue
                k=v
                visited.add(k)
                ans.append(k)
        return ans