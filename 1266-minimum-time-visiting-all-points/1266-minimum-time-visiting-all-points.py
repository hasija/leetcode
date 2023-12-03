class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        start = points[0]
        ans = 0
        for x,y in points[1:]:
            x1 = abs(start[0]-x)
            y1 = abs(start[1]-y)
            start = [x,y]
            ans += max(x1,y1)
        return ans