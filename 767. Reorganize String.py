from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = dict(Counter(s))
        final_arr = [(-val,key) for key,val in cnt.items()]
        heapq.heapify(final_arr)
        prev_key, prev_val = '',0
        final_res = ""
        while final_arr:
            val, key = heapq.heappop(final_arr)
            final_res+=key
            val+=1
            if prev_val<0:
                heapq.heappush(final_arr,(prev_val, prev_key))
            prev_key, prev_val = key, val
        if len(final_res)!=len(s):
            return ""
        else:
            return final_res
            