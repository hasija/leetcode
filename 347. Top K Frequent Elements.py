import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in range(len(nums)):
            if nums[x] in freq:
                freq[nums[x]]+=1
            else:
                freq[nums[x]] = 1
        freq_arr = [(-v,k) for k,v in freq.items()]
        maxheap = heapq.heapify(freq_arr)
        final_arr = []
        for x in range(k):
            final_arr.append(heapq.heappop(freq_arr)[1])
            
        return final_arr