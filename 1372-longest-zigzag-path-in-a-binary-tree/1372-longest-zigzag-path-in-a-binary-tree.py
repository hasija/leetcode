# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def dfs(node):
            if node:
                l = dfs(node.left)
                r = dfs(node.right)
                # print (l, r,'returnes')
                left = 1+l[1] if node.left else 0
                right = 1+r[0] if node.right else 0
                self.max = max(self.max, left, right)
                out = [left, right]
                return out
            else:
                return [0,0]
        dfs(root)
        return self.max