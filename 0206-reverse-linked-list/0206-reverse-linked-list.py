# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.new_head = None
        def dfs(node):
            if node:
                
                next_node = dfs(node.next)
                if next_node:
                    next_node.next = node
                else:
                    self.new_head = node
                
                return node
            return None
        dfs(head)
        if head:
            head.next = None
        return self.new_head