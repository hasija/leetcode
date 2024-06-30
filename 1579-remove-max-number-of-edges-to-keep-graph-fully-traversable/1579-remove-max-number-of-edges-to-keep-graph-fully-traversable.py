class UnionFind:
    def __init__(self, n):
        self.n = n
        self.graph = [i for i in range(n+1)]
        self.rank = [0]*(self.n+1)
    
    def join(self, l,r):
        p1 = self.find(l)
        p2 = self.find(r)
        if p1!=p2:
            if self.rank[p1]>=self.rank[p2]:
                self.graph[p2]=p1
                self.rank[p1]+=self.rank[p2]+1
            else:
                self.graph[p1]=p2
                self.rank[p2]+=self.rank[p1]+1
            return True
        else:
            return False
    
    def find(self, node):
        if self.graph[node]!=node:
            self.graph[node] = self.find(self.graph[node])
        return self.graph[node]
        
    def connected(self):
        parent = set()
        for i in range(1, self.n+1):
            parent.add(self.find(i))
        if len(parent)>1:
            return False
        return True
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges = sorted(edges, key = lambda x: -x[0])
        uf1 = UnionFind(n)
        uf2 = UnionFind(n)
        
        count = 0
        for t,l,r in edges:
            # print ("edges", t,l,r, count)
            if t==3 and uf1.join(l,r):
                uf2.join(l,r)
                count+=1
            elif t==2 and uf1.join(l,r):
                count+=1
            elif t==1 and uf2.join(l,r):
                count+=1
            # print ("Counter after using edge", count)
        
        if uf1.connected() and uf2.connected():
            return len(edges)-count
        return -1
                
                