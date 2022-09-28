# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.count = 0
        self.len = 0
        self.head = head
        def dfs(node):
            if node:
                self.len+=1
                dfs(node.next)
                self.count+=1
                if self.len==n and self.count==n:
                    self.head = node.next
                if self.count==n+1:
                    node.next = node.next.next
        dfs(head)
        return self.head
        