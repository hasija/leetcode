# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, arr):
            if node:
                if node.left:
                    dfs(node.left, arr+[node.val])
                if node.right:
                    dfs(node.right, arr+[node.val])
                if not node.left and not node.right:
                    out = int(''.join(map(str, arr+[node.val])))
                    self.ans+=out
            else:
                pass
        dfs(root, [])
        return self.ans
        