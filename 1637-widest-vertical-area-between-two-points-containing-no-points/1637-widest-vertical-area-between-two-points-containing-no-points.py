class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = []
        for i,j in points:
            x_points.append(i)
        x_points.sort()
        prev = x_points[0]
        dist = 0
        for i in x_points[1:]:
            dist =max(dist, i-prev)
            prev = i
        return dist
            