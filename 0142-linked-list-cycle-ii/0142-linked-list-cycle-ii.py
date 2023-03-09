# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_set = set()
        while True:
            if not head:
                return None
            if head not in node_set:
                node_set.add(head)
                head = head.next
            else:
                return head
        return None
        