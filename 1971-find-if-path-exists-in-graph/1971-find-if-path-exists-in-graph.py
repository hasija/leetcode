class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path = defaultdict(set)
        for i,j in edges:
            path[i].add(j)
            path[j].add(i)
        visited = set([source])
        to_visit_arr = [source]
        while to_visit_arr:
            new_visits = set()
            for to_visit in to_visit_arr:
                if to_visit == destination:
                    return True
                visited.add(to_visit)
                for v in path[to_visit]:
                    if v not in visited:
                        new_visits.add(v)
            to_visit_arr = new_visits
        return False
                    