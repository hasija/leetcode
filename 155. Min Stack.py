class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dict={}
        self.key=0
    def push(self, val: int) -> None:
        self.dict[self.key+1]={"val":val}
        if self.key in self.dict and val<self.dict[self.key]['min_val']:
            self.dict[self.key+1]['min_val']=val
        elif self.key in self.dict:
            self.dict[self.key+1]['min_val']=self.dict[self.key]['min_val']
        else:
            self.dict[self.key+1]['min_val']=val
        self.key+=1
        
    def pop(self) -> None:
        self.dict.pop(self.key)
        self.key-=1
        
    def top(self) -> int:
        return self.dict[self.key]['val']

    def getMin(self) -> int:
        return self.dict[self.key]['min_val']


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()