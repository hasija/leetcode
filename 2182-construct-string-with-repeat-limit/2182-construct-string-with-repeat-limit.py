class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        arr = []
        for k,v in cnt.items():
            heapq.heappush(arr, (-(ord(k)-97), k, v))
        
        ans = ""
        # print(arr)
        while arr:
            vals = list(heapq.heappop(arr))
            # print("looping ", vals)
            while vals[2]-repeatLimit>0:
                ans+=vals[1]*repeatLimit
                # print ("adding", vals[1])
                vals[2]-=repeatLimit
                if arr:
                    next_val = list(heapq.heappop(arr))
                    ans+=next_val[1]
                    next_val[2]-=1
                    if next_val[2]>0:
                        heapq.heappush(arr, tuple(next_val))
                else:
                    return ans
            ans+=vals[1]*vals[2]
        return ans