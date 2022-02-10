import statistics
import math
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        counter = 0
        max_val = -float(inf)
        start = 0
        for x in range(len(seats)):
            counter+=1
            # print (x, counter, start, max_val)
            if seats[x]==1 or x==len(seats)-1:
                if seats[x]!=1:
                    seat_val = len(seats)-1
                elif start == 0 and seats[0]!=1:
                    seat_val = 0
                else:
                    seat_val = math.floor(statistics.median([y for y in range(counter)]))
                    seat_val = start+seat_val
                if x==len(seats)-1 and seats[x]!=1:
                    dist_from_right = float(inf)
                else:
                    dist_from_right = x - seat_val
                if start == 0 and seats[0]!=1:
                    dist_from_left = float(inf)
                else:
                    dist_from_left = seat_val - start
                # print(f"right: {dist_from_right}")
                # print(f"left: {dist_from_left}")
                # print(min(dist_from_left,dist_from_right))
                if min(dist_from_left,dist_from_right) > max_val:
                    max_val = min(dist_from_left,dist_from_right)
                start = x
                counter = 1
        return max_val
        