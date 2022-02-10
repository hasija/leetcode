# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter=1
        start = head
        new_head = ListNode()
        new_head_start = new_head
        prev_node = None
        while head:
            if counter%2==0:
                # print (head.val)
                prev_node.next=head.next
                new_head.next = head
                # print (new_head_start)
                head = head.next
                new_head = new_head.next
                counter+=1
            else:
                prev_node = head
                head = head.next
                counter+=1
        if counter>1:
            new_head.next = None
            prev_node.next = new_head_start.next
        # print (new_head_start)

        # while start:
        #     # print (start.val)
        #     start = start.next
        return start