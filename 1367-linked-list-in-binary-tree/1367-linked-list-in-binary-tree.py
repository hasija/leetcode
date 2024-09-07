# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        self.ans = False
        def dfs(node):
            if self.ans:
                return 
            
            if node:
                if node.val == head.val:
                    check_tree(node, head)
                dfs(node.left)
                dfs(node.right)
        
        def check_tree(node, l_node):
            if self.ans:
                return
            if l_node is None:
                self.ans = True
                return
            if node is None:
                return
            if node.val == l_node.val:
                check_tree(node.left, l_node.next)
                check_tree(node.right, l_node.next)
            
                
        
        dfs(root)
        return self.ans
            