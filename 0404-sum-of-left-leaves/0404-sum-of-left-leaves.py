# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def dfs(node, posi):
            if node:
                dfs(node.left, 'left')
                if posi == 'left' and node.left is None and node.right is None:
                    # print ("is it left", node.val)
                    self.count+=node.val
                dfs(node.right, 'right')
        dfs(root, None)
        return self.count