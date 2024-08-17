class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])
        prev_row = points[0]
        for row in range(1, rows):
            # print ("prev row", prev_row)
            left_max = [0]*cols
            right_max = [0]*cols
            curr_row = [0]*cols
            left_max[0] = prev_row[0]
            for l in range(1, cols):
                left_max[l] = max(left_max[l-1]-1, prev_row[l])
                
            right_max[cols-1] = prev_row[cols-1]
            for r in range(cols-2,-1,-1):
                right_max[r] = max(right_max[r+1]-1, prev_row[r])
            # print ("l and r", left_max, right_max)
            for i in range(cols):
                # print ("Looping", left_max[i], right_max[i], points[row][i])
                curr_row[i]=max(left_max[i], right_max[i])+points[row][i]
                
            prev_row=curr_row
            
        return max(prev_row)
                
                