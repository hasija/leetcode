import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [i for i in range(1, 1001)]
        self.set = set(self.arr)
        heapq.heapify(self.arr)
        
    def popSmallest(self) -> int:
        val = heapq.heappop(self.arr)
        self.set.remove(val)
        return val
        

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
            heapq.heappush(self.arr, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)