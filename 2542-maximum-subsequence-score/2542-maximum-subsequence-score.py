class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = list(zip(nums2, nums1))
        arr = sorted(arr, key= lambda x: -x[0])
        sum_heap_arr = []
        max_v = -float('inf')
        s = 0
        for i in range(len(arr)):
            val = arr[i]
            if i<k-1:
                heapq.heappush(sum_heap_arr, val[1])
                s+=val[1]
            else:
                # print (sum_heap_arr)
                # s = sum(sum_heap_arr)
                s_new=s+val[1]
                final = s_new*val[0]
                max_v = max(final, max_v)
                if sum_heap_arr and val[1]>sum_heap_arr[0]:
                    x=heapq.heappop(sum_heap_arr)
                    s-=x
                    heapq.heappush(sum_heap_arr, val[1])
                    s+=val[1]


            
        return max_v    
        