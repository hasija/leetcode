class LinkedList():
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
        
class MyCircularDeque:

    def __init__(self, k: int):
        self.root = LinkedList()
        self.n = k
        self.used = 0
        self.last_node = LinkedList()
        self.root.next = self.last_node
        self.last_node.prev = self.root
        
    def insertFront(self, value: int) -> bool:
        # print ("here1")
        if self.used<self.n:
            new_node = LinkedList(value)
            old_nxt_node = self.root.next
            self.root.next = new_node
            new_node.prev = self.root
            new_node.next = old_nxt_node
            old_nxt_node.prev = new_node
            self.used+=1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        # print ("here2")
        if self.used<self.n:
            new_node = LinkedList(value)
            old_last_node = self.last_node.prev
            old_last_node.next = new_node
            new_node.next = self.last_node
            new_node.prev = old_last_node
            self.last_node.prev = new_node
            self.used+=1
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        # print ("here3")
        if self.used>=1:
            self.used-=1
            front_node = self.root.next
            self.root.next = front_node.next
            self.root = self.root.next.prev
            return True 
        return False
    def deleteLast(self) -> bool:
        # print ("here4")
        if self.used>=1:
            self.used-=1
            prev_node = self.last_node.prev.prev
            prev_node.next = self.last_node
            self.last_node.prev = prev_node
            return True
        return False

    def getFront(self) -> int:
        # print ("here5")
        if self.used>=1:
            return self.root.next.val
        return -1
    def getRear(self) -> int:
        # print ("here6")
        if self.used>=1:
            print 
            return self.last_node.prev.val
        return -1
    
    def isEmpty(self) -> bool:
        # print ("here7")
        if self.used==0:
            return True
        return False

    def isFull(self) -> bool:
        # print ("here8")
        if self.used==self.n:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()