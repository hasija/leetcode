class MyQueue:

    def __init__(self):
        self.in_elem = []
        self.out = []
        self.len = 0
        

    def push(self, x: int) -> None:
        self.in_elem.append(x)
        self.len+=1
    def pop(self) -> int:
        self.len-=1
        if self.out:
            return self.out.pop()
        else:
            while self.in_elem:
                self.out.append(self.in_elem.pop())
        
        return self.out.pop()
    
    def peek(self) -> int:
        if self.out:
            return self.out[-1]
        else:
            return self.in_elem[0]

    def empty(self) -> bool:
        print(self.len)
        if self.len==0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()