# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        start = head
        old_node = head
        def sort(node, start_node):
            old_node=None
            while (True):
                if node.val >=start_node.val:
                    old_node = start_node
                    start_node =start_node.next
                else:
                    if old_node:
                        n=old_node.next
                        old_node.next=node
                        next_node = node.next
                        node.next = n
                        return next_node
                    else:
                        head = node
                        next_node = node.next
                        head.next = start_node
                        return next_node
        if head.next:
            curr_node = head.next
            while(curr_node):
                if curr_node.val>=old_node.val:
                    old_node = curr_node
                    curr_node = curr_node.next
                else:
                    curr_node = sort(curr_node, start)
        return head