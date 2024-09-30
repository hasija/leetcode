class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.n = maxSize
        self.cnt = 0

    def push(self, x: int) -> None:
        if self.cnt<self.n:
            self.cnt+=1
            self.arr.append(x)
        return

    def pop(self) -> int:
        if self.arr:
            self.cnt-=1
            return self.arr.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(self.cnt, k)):
            self.arr[i]+=val
    


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)