# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.node = head
        self.flag = True
        node = head
        def dfs(node):
            if node:
                dfs(node.next)
                if node.val!=self.node.val:
                    self.flag=False
                self.node = self.node.next
        dfs(node)
        if self.flag:
            return True
        else:
            return False