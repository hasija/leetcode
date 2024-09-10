# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        while start:
            first = start
            second = start.next
            if second is None:
                return head
            
            new_val = math.gcd(first.val,second.val)
            node = ListNode(val=new_val, next=second)
            first.next = node
            start = start.next.next
            
            