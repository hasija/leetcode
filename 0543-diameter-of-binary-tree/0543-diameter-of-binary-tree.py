# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def dfs(node):
            if node:
                left_cnt = dfs(node.left)
                right_cnt = dfs(node.right)
                self.max = max(left_cnt+right_cnt, self.max)
                node_max = max(left_cnt, right_cnt)
                return node_max+1
            else:
                return 0
        dfs(root)
        return self.max
                