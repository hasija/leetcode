class Tree:
    def __init__(self, node=None, next=[], dist=[]):
        self.node = node
        self.next = next
        self.dist=dist
    def add(self, val, dist):
        self.next.append(val)
        self.dist.append(dist)
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.min = float('inf')
        # Map
        map_road = {}
        for i ,j ,d in roads:
            if i not in map_road:
                map_road[i]=Tree(node=i, next=[j], dist=[d])
            else:
                map_road[i].add(j, d)
            if j not in map_road:
                map_road[j]=Tree(node=j, next=[i], dist=[d])
            else:
                map_road[j].add(i, d)
        # print (map_road[1].next)
        self.visited = set()
        def dfs(city):

            # print ('iterate',city)
            # if city == n:
            #     return
            if city in self.visited:
                return
            self.visited.add(city)

            # print ("cities to visit", map_road[city].next)
            for ind, new in enumerate(map_road[city].next):
                # print ("here 3")
                new_d = map_road[city].dist[ind]
                self.min = min(new_d, self.min)
                dfs(new)
        dfs(1)
        return self.min