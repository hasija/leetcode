# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, prev):
            if node:
                right = dfs(node.right, prev)
                curr = node.val
                node.val = right+curr
                left= dfs(node.left, node.val)
                return left
            else:
                return prev
        dfs(root, 0)
        return root