from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.hash = SortedDict()
        

    def book(self, start: int, end: int) -> int:
        self.hash[start] = self.hash.get(start, 0)+1
        self.hash[end] = self.hash.get(end, 0)-1
        res = 0
        tmp = 0
        for val in self.hash.values():
            tmp+=val
            res = max(tmp, res)
        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)