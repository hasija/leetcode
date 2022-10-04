# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.out = False
        if root is None :
            return False
        def dfs(node, num):
            if node:
                num+=node.val
                if node.left:
                    dfs(node.left, num)
                if node.right:
                    dfs(node.right, num)

                if node.left is None and node.right is None:
                    if num==targetSum:
                        self.out=True
        dfs(root, 0)
        return self.out