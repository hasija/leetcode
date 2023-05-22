class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        
        c_dict = collections.defaultdict(int)
        arr = []
        curr_set = set()
        for val in nums:
            c_dict[val]+=1
        
        for key,v in c_dict.items():
            if key not in curr_set and heap and v>heap[0][0]:
                heapq.heappush(heap ,(v,key))
                curr_set.add(key)
                if len(heap)>k:
                    out = heapq.heappop(heap)
                    curr_set.remove(out[1])
            elif len(heap)<k:
                curr_set.add(key)
                heapq.heappush(heap ,(v,key))
        return [v[1] for v in heap]
    

                
        