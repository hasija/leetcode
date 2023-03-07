class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time = sorted(time)
        self.found = float('inf')
        def get_trips(t):
            trips = sum([t//i for i in time ])
            return trips
        
        def search(l,r):
            # print ("Iterating",l,r, (l+r)//2)
            if l<=r:
                mid = (l+r)//2
                trips = get_trips(mid)
#                 if trips==totalTrips:
#                     print ("found")
#                     self.found = min(self.found, mid)
                
                # print ("Trips", trips)
                if trips>=totalTrips:
                    self.found = min(self.found, mid)
                    r=mid-1
                else:
                    l=mid+1
                return search(l,r)
            else:
                return
            
        
        
        l = 1
        r = totalTrips*time[0]
        
        res = search(l,r)
        return self.found
        