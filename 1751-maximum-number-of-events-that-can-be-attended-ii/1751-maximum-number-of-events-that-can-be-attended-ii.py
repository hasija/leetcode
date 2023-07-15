class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        dp = {}
        
        events = sorted(events, key=lambda x: (x[0],x[1]))
        start_arr = [val[0] for val in events]
        
        
        def find(idx, count):
            if count==k or idx>=len(events):
                return 0
            
            if (idx, count) in dp:
                return dp[(idx, count)]
            
            # Two choices
            curr = events[idx]
            next_ind = bisect.bisect_left(start_arr, curr[1]+1)
            v1 = curr[2]+ find(next_ind, count+1)
            v2 = find(idx+1, count)
            dp[(idx, count)]=max(v1, v2)
            return dp[(idx, count)]
        return find(0,0)
            