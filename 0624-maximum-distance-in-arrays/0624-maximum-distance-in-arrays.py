class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_arr = [(i[0],idx) for idx,i in enumerate(arrays)]
        max_arr = [(-i[-1],idx) for idx,i in enumerate(arrays)]
        
        heapq.heapify(min_arr)
        heapq.heapify(max_arr)
        if min_arr[0][1]==max_arr[0][1]:
            first_pass_min = heapq.heappop(min_arr)
            first_pass_max = heapq.heappop(max_arr)
            # print((-max_arr[0][0]-first_pass_min[0], 
            #            -first_pass_max[0]-min_arr[0][0]))
            return max(-max_arr[0][0]-first_pass_min[0], 
                       -first_pass_max[0]-min_arr[0][0])
        else:
            return -max_arr[0][0]-min_arr[0][0]