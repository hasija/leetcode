class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def get_flowers(mid):
            cnt = 0
            total = 0
            for day in bloomDay:
                if day<=mid:
                     cnt+=1
                else:
                    cnt = 0
                if cnt==k:
                    total+=1
                    cnt = 0
            return total

        
        
        
        if m*k>len(bloomDay):
            return -1
        
        s = 0
        e = max(bloomDay)
        ans = e
        while (s<=e):
            mid = (s+e)//2        
            out = get_flowers(mid)
            if out>=m:
                ans = min(ans, mid)
                e = mid-1
            else:
                s=mid+1
        return ans
       