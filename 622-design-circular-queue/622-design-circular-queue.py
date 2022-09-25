class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None]*k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            ind = (self.head+self.count)%self.size
            self.queue[ind]=value
            self.count+=1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = (self.head+1)%self.size
            self.count-=1
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.head]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.head+self.count-1)%self.size]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.count ==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.count == self.size:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()