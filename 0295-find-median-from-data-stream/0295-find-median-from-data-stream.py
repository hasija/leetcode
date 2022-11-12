class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.big):
            heapq.heappush(self.big, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.big, num))
        
    def findMedian(self) -> float:
        if len(self.small)==len(self.big):
            return (-self.small[0]+self.big[0])/2
        else:
            return self.big[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()