# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        watch_arr=set()
        output=False
        while True:
            if head and head.next:
                if head.next in watch_arr:
                    output=True
                    break
                watch_arr.add(head.next)
                head=head.next
            else:
                break
        return output
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        watch_arr=set()
        output=False
        head2=head
        while True:
            if head and head.next and head2 and head2.next and head2.next.next:
                head=head.next
                head2=head2.next.next
                if head2==head:
                    output=True
                    break
            else:
                break
        return output