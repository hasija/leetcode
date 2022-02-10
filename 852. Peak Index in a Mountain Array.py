class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ind_val = None
        prev_val = None
        flag_count = 0
        asc = False
        dsc = None
        for x in range(len(arr)):
            if prev_val is None:
                prev_val = arr[x]
                continue
            if prev_val < arr[x]:
                asc=True
                prev_val =arr[x]
            elif prev_val > arr[x]:
                return x-1
    
    

import math
class Solution:
    def check_cond(self, arr, x):
        if arr[x-1]<arr[x] and arr[x+1]<arr[x]:
            return True, None
        elif arr[x-1]<arr[x] and arr[x]<arr[x+1]:
            return False, 'left'
        elif arr[x+1]<arr[x] and arr[x-1]>arr[x]:
            return False, 'right'
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        print (arr)
        l=0
        h=len(arr)-1
        for q in range(len(arr)):
            if l==h:
                out , res = check_cond(arr, l)
                if out:
                    return l
            median=math.floor((h-l+2)/2)+l-1
            out, res= self.check_cond(arr, median)
            if out:
                return median
            elif res=='left':
                l=median
            elif res=='right':
                h=median
            