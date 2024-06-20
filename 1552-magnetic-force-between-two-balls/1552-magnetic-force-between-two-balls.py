class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        s = 0
        e = position[-1]
        ans = -1
        
        def check_posible(diff):
            last = None
            cnt = 1
            for i in position:
                if last is None:
                    last = i
                    continue
                elif i-last>=diff: 
                    cnt+=1
                    last = i
                if cnt==m:
                    return True
            return False
        
        while (s<=e):
           
            mid = (s+e)//2
            # print ("mid value", mid, s, e)
            if check_posible(mid):
                ans = max(ans, mid)
                s = mid+1
            else:
                e = mid-1
            
        return ans
            