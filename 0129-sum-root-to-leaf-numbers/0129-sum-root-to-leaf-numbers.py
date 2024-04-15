# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 
        def dfs(node, past):
            if node:
                if node.left is None and node.right is None:
                    self.ans+=int(past+str(node.val))
                dfs(node.left, past+str(node.val))
                dfs(node.right, past+str(node.val))
        dfs(root, '')
        return self.ans
                
                    