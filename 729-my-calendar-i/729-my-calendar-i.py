class Node:
    def __init__(self,start, end):
        self.left = None
        self.right = None
        self.end = end
        self.start = start

        
class MyCalendar:
    
    def insert(self, node, parent):
        if node.start>=parent.end:
            if parent.right is None:
                parent.right = node
                return True
            return self.insert(node, parent.right)
        if node.end<=parent.start:
            if parent.left is None:
                parent.left = node
                return True
            return self.insert(node, parent.left)
        return False            
    
    
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        node = Node(start, end)
        if self.root is None:
            self.root = node
            return True

        return self.insert(node, self.root)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)