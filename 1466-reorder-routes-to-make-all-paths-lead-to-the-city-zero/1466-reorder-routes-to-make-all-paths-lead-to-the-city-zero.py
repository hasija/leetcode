class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        h_map = {}
        for i, j in connections:
            if i not in h_map:
                h_map[i]={'in':set(), 'out':set()}
            if j not in h_map:
                h_map[j]={'in':set(), 'out':set()}
            h_map[i]['in'].add(j)
            h_map[j]['out'].add(i)
        
        self.total = 0
        self.visited = set()
        def dfs(val):
            # print ("iterating", val)
            total = 0
            # print ("total out", h_map[val]['in'])
            for out in h_map[val]['in']:
                if out in self.visited:
                    continue
                # print ("looping out", out)
                self.visited.add(out)
                total+=dfs(out)
                self.visited.remove(out)
                self.visited
                # print ("total val for out", out, total)
                total+=1
            for out in h_map[val]['out']:
                if out in self.visited:
                    continue
                self.visited.add(out)
                total+=dfs(out)
                self.visited.remove(out)
            # print ("final val of num", val , total)
            return total
        self.visited.add(0)
        return dfs(0)
        