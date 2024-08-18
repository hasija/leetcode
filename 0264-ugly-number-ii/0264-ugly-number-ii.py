class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_arr = [1]
        seen_set = set()
        for i in range(n-1):
            min_val = heapq.heappop(ugly_arr)
            if min_val*2 not in seen_set:
                heapq.heappush(ugly_arr, min_val*2)
                seen_set.add(min_val*2)
            if min_val*3 not in seen_set:
                seen_set.add(min_val*3)
                heapq.heappush(ugly_arr, min_val*3)
            if min_val*5 not in seen_set:
                seen_set.add(min_val*5)
                heapq.heappush(ugly_arr, min_val*5)
            # print("min val found", min_val)
        return heapq.heappop(ugly_arr)