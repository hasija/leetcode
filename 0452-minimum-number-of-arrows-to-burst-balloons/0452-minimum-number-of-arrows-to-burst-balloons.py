class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arr = sorted(points, key = lambda x : (x[0],x[1]))
        prev = None
        ans = 0
        for i in arr:
            if prev is None:
                ans+=1
                prev = i
            elif (i[0]<=prev[1] and prev[0]<=i[1]) or (prev[0]<=i[1] and i[0]<=prev[1]):
                    prev = [max(prev[0],i[0]),min(prev[1],i[1])]
            else:
                prev = i
                ans+=1
        return ans
                
        