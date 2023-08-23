class Solution:
    def reorganizeString(self, s: str) -> str:
        h_map = dict(Counter(s))
        arr = [[-v,k] for k,v in h_map.items()]
        heapq.heapify(arr)
        new_s = ""
        while len(arr)>1:
            f = heapq.heappop(arr)
            s = heapq.heappop(arr)
            new_s += f[1]+s[1]
            
            f[0]+=1
            s[0]+=1
            if f[0]!=0:
                heapq.heappush(arr, [f[0], f[1]])
            if s[0]!=0:
                heapq.heappush(arr, [s[0], s[1]])
            
            # out = f[0]-s[0]
            # new_s += ''.join([f"{f[1]}{s[1]}" for i in range(abs(s[0]))])
            # if out!=0:
                # heapq.heappush(arr, (out, f[1]))
        if arr:
            val = -arr[0][0]
            if val>1:
                return ""
            return new_s+arr[0][1]
        else:
            return new_s
        