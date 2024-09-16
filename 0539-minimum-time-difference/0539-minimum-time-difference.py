class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_ = float('inf')
        n = len(timePoints)
        def get_mins(t):
            curr = int(t[:2])*60
            curr+= int(t[3:])
            return curr
        
        arr = []
        for i in timePoints:
            arr.append(get_mins(i))
        
        arr.sort()
        last = (1440-arr[-1])*-1
        for i in arr:
            min_ = min((i-last),min_)
            last = i
        return min_