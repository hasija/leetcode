class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        hmap = {}
        for i in range(n):
            hmap[i]=0
        for u,v in edges:
            hmap[v]+=1
        flag = True
        for i,j in hmap.items():
            if j==0 and flag:
                ans = i
                flag = False
            elif j==0 and flag is False:
                return -1
        return ans