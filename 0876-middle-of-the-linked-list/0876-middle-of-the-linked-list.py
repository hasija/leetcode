# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node = head
        while node:
            count+=1
            node=node.next
        count = count//2
        c = 0
        node = head
        while c!=count:
            node = node.next
            c+=1
        return node
            