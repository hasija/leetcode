class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = [i for i in nums]
        heapq.heapify(self.arr)

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        arr = []
        while len(self.arr)!=self.k:
            heapq.heappop(self.arr)
        return self.arr[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)