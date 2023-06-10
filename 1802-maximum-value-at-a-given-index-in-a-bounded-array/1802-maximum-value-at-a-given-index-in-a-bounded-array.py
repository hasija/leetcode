class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def get_sum(val):
            count = 0
            #Positive case Left
            if val-1-(index)>=0:
                count+= (val*(val+1))//2
                # Subtract overspill
                last_num = val-index-1
                sub = (last_num*(last_num+1))//2
                count-=sub
            # Case with 1 extras
            else:
                count+= (val*(val+1))//2
                last_num = abs(val-index-1)
                count+= last_num
            
            # Righ case
            
            if val-1-(n-1-index)>=0:
                #positive case
                count+=val*(val+1)//2
                #sub overspill
                last_num = (val-(n-1-index)-1)
                sub = (last_num*(last_num+1))//2
                count-=sub
            else:
                count+=val*(val+1)//2
                last_num = abs((val-(n-1-index)-1))
                count+=last_num
                
            count-=val
            return count
        
        l = 0
        r = maxSum
        while l<r:
            # print("iterating",l,r)
            mid = (l+r+1)//2
            if get_sum(mid) <= maxSum:
                l=mid
            else:
                r = mid-1
            
        return l
        
        
                
                
            
            