class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        r = 10**7
        l = 1
        self.out = -1
        def on_time(s):
            total = 0
            for i in range(len(dist)):
                d = dist[i]
                t = d/s
                if i<len(dist)-1:
                    t = ceil(t)
                total+=t
            if total<=hour:
                return True
            else:
                return False
                
        
        while l<=r:
            # print (l,r)
            mid = (l+r)//2
            if on_time(mid):
                r=mid-1
                self.out = mid
            else:
                l=mid+1
        return self.out