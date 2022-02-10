class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        out = self.find_largest()
        return out

    def find_largest(self):
        self.nums.sort()
        return self.nums[-self.k]



["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
["KthLargest","add","add","add","add","add"]
[[1,[]],[-3],[-2],[-4],[0],[4]]

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        heapq.heapify(self.nums)
        while(len(self.nums)>self.k):
            heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        # print (f"val: {val}")
        if len(self.nums)<self.k:
            heapq.heappush(self.nums, val)
        else:
            heapq.heappushpop(self.nums, val)
        # print (self.nums)
        return self.nums[0]
        