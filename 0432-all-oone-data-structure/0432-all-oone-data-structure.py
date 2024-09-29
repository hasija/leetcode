class LinkedList:
    def __init__(self, cnt=0):
        self.cnt = cnt
        self.next = None
        self.prev = None
        self.keys = set()
        
class AllOne:

    def __init__(self):
        self.map = {}
        self.head = LinkedList()
        self.tail = LinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cnt_map = {}
        
    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            prev_key_node = node
            node.keys.remove(key)
            
            if node.prev.cnt == node.cnt+1:
                node = node.prev
            else:
                new_node = LinkedList(cnt=node.cnt+1)
                old_prev = node.prev
                old_prev.next = new_node
                new_node.prev = old_prev
                new_node.next = node
                node.prev = new_node
                node = new_node

            if not prev_key_node.keys:
                self.remove_node(prev_key_node)
                
        else:
            cnt = 1
            if self.tail.prev.cnt == 1:
                node = self.tail.prev
            else:
                node = LinkedList(cnt=1)
                old = self.tail.prev
                old.next = node
                node.prev = old
                node.next = self.tail
                self.tail.prev = node
        # print ("This is node", node)
        node.keys.add(key)
        self.map[key]=node

            
    def dec(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            node.keys.remove(key)
            prev_key_node = node


            if node.next.cnt == node.cnt-1 and node.next.cnt!=0:
                node = node.next
            elif node.cnt-1>0:
                new_node = LinkedList(cnt=node.cnt-1)
                old_next = node.next
                new_node.prev = node
                node.next = new_node
                new_node.next = old_next
                old_next.prev = new_node
                node = new_node
            else:
                self.map.pop(key)

            if not prev_key_node.keys:
                self.remove_node(prev_key_node)
        if prev_key_node.cnt!=1:
            node.keys.add(key)
            self.map[key]=node
  

    def getMaxKey(self) -> str:
        if self.head.next.cnt>0:
            first = self.head.next.keys.pop()
            self.head.next.keys.add(first)
            return first
        return ""

    def getMinKey(self) -> str:
        if self.tail.prev.cnt>0:
            first = self.tail.prev.keys.pop()
            self.tail.prev.keys.add(first)
            return first
        return ""

    def remove_node(self, node):
        old = node.prev
        new = node.next
        old.next = new
        new.prev = old
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()