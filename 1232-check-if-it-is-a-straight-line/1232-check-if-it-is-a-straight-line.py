class Solution:
    def checkStraightLine(self, arr: List[List[int]]) -> bool:
        x1,y1=arr[0]
        x2,y2=arr[1]
        try:
            m = (y2-y1)/(x2-x1)
        except:
            m = None
        
        n = len(arr)
        
        for i in range(2, n):
            x, y = arr[i]
            try:
                new_m = (y-y2)/(x-x2)
            except:
                new_m = None
            if new_m!=m:
                return False
            x2 = x
            y2 = y
        return True
        
        