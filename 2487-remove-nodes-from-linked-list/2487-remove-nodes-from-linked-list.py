# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        prev = None
        while arr:
            value = arr.pop()
            if prev is None:
                node = ListNode(val=value, next = prev)
                prev = node
            else:
                if prev.val<=value:
                    node = ListNode(val=value, next = prev)
                    prev = node
        return node
            
            
            
            
        
        
        
    