class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = []
        if a:
            arr.append((-a, 'a'))
        if b:
            arr.append((-b, 'b'))
        if c:
            arr.append((-c, 'c'))
        heapq.heapify(arr)
        ans = ""
        while arr:
            # print ("arr", arr)
            # print("ans", ans)
            cnt, char = heapq.heappop(arr)
            if len(ans)>=2 and ans[-1]==char and ans[-2]==char and arr:
                nxt_cnt, nxt_char = heapq.heappop(arr)
                nxt_cnt_taken = 1
                ans+=nxt_char*nxt_cnt_taken
                nxt_cnt+=nxt_cnt_taken
                if nxt_cnt!=0:
                    heapq.heappush(arr, (nxt_cnt, nxt_char))
                if cnt!=0:
                    heapq.heappush(arr, (cnt, char))
            elif len(ans)>=2 and ans[-1]==char and ans[-2]==char and not arr:
                break
            else:
                cnt_taken = 1
                ans+=char*cnt_taken
                cnt+=cnt_taken
                if cnt!=0:
                    heapq.heappush(arr, (cnt, char))
                
        return ans