"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        created = {}
        new_head = Node(x=-1)
        s = new_head
        while head:
            if head.random and head.random not in created:
                created[head.random] = Node(x=head.random.val)
            
            random = created[head.random] if head.random else None
            
            if head not in created:
                new = Node(x=head.val, random=random)
                created[head] = new
            else:
                new = created[head]
                new.random=random
            s.next = new
            s = s.next
            head = head.next
        return new_head.next