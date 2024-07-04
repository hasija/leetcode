# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        tmp = None
        while head:
            if head.val==0:
                if tmp:
                    arr.append(tmp)
                tmp=0
            else:
                tmp+=head.val
            head=head.next
        root = ListNode()
        last = root
        for val in arr:
            node = ListNode(val=val)
            last.next = node
            last = node
        
        return root.next