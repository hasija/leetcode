class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def get_coordinates(x1,x2,y1,y2):
            return {0:[x1,y1],1:[x2,y1],2:[x2,y2],3:[x1,y2]}
        
        first = get_coordinates(ax1,ax2,ay1,ay2)
        second = get_coordinates(bx1,bx2,by1,by2)
        
        def left_overlap(a,b):
            if b[0][0]>=a[0][0] and b[0][0]<a[1][0] and b[1][0]>=a[1][0]:
                return abs(b[0][0]-a[1][0])
            if a[0][0]>=b[0][0] and a[0][0]<b[1][0] and a[1][0]>=b[1][0]:
                return abs(a[0][0]-b[1][0])
            if b[0][0]>=a[0][0] and b[0][0]<a[1][0] and b[1][0]<a[1][0]:
                return abs(b[1][0]-b[0][0])
            if a[0][0]>=b[0][0] and a[0][0]<b[1][0] and a[1][0]<b[1][0]:
                return abs(a[1][0]-a[0][0])
        
        def top_overlap(a,b):
            if b[0][1]>=a[0][1] and b[0][1]<a[2][1] and b[2][1]>=a[2][1]:
                return abs(b[0][1]-a[2][1])
            if a[0][1]>=b[0][1] and a[0][1]<b[2][1] and a[2][1]>=b[2][1]:
                return abs(a[0][1]-b[2][1])
            if b[0][1]>=a[0][1] and b[0][1]<a[2][1] and b[2][1]<a[2][1]:
                return abs(b[2][1]-b[0][1])
            if a[0][1]>=b[0][1] and a[0][1]<b[2][1] and a[2][1]<b[2][1]:
                return abs(a[2][1]-a[0][1])
        
        l=left_overlap(first,second)
        t=top_overlap(first, second)
        
        total_area = (first[1][0]-first[0][0])*(first[2][1]-first[0][1])
        total_area+=(second[1][0]-second[0][0])*(second[2][1]-second[0][1])
        if l is not None and t is not None:
            total_area -=l*t
        return total_area
        