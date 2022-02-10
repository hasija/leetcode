"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        mapping_dict = {}
        counter = 0
        new_head = None
        old_head = head
        old = None
        while(head):
            if head not in mapping_dict:
                mapping_dict[head] = Node(head.val)
            if old:
                old.next = mapping_dict[head]
            else:
                new_head = mapping_dict[head]
            if head.random is None:
                pass
            elif head.random in mapping_dict:
                mapping_dict[head].random = mapping_dict[head.random]
            else:
                mapping_dict[head.random] = Node(head.random.val)
                mapping_dict[head].random = mapping_dict[head.random]
            old = mapping_dict[head]
            head = head.next
        return new_head


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        start = head
        while (head):
            tmp = Node(head.val)
            tmp.next = head.next
            head.next = tmp
            head = tmp.next
        
        head = start
        
        while(head):
            if head.random is None:
                pass
            elif head.next:
                head.next.random = head.random.next
            head = head.next.next
        if start is None:
            return start
        head = start.next
        while (head):
            if head.next and head.next.next:
                head.next = head.next.next
            head = head.next
        return start.next
