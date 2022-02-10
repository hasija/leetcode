# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        start = head
        prev=None
        curr=None
        head_new = None
        pre_prev = None
        def swap_nodes(prev, curr, pre_prev):
            tmp = curr.next
            curr.next = prev
            prev.next = tmp
            if pre_prev:
                pre_prev.next=curr
            return prev, curr
        while (start):
            if not prev:
                prev = start
                start= start.next
                continue
            else:
                curr = start
                start, tmp_node = swap_nodes(prev,curr, pre_prev)
                if not head_new:
                    head_new = tmp_node
                pre_prev = start
                start = start.next
                prev=None
        if head_new:
            return head_new
        else:
            return head