# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cnt = 0
        pre_node = ListNode(next=list1)
        head = pre_node
        head2 = list2
        prev_head = None
        while head2:
            prev_head = head2
            head2 = head2.next


        while head:
            if cnt==a:
                a_head = head
            if cnt==b:
                b_head = head
            head= head.next
            cnt+=1
        prev_head.next = b_head.next.next
        a_head.next = list2
        return pre_node.next
            
                