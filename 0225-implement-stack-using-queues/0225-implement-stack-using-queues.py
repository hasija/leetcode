class MyStack:

    def __init__(self):
        self.arr=[]
        self.length = 0
    
    def push(self, x: int) -> None:
        self.arr.append(x)
        self.length+=1

    def pop(self) -> int:
        val = self.arr[-1]
        del self.arr[-1]
        self.length-=1
        return val
    
    def top(self) -> int:
        return self.arr[-1]

    def empty(self) -> bool:
        return self.length == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()