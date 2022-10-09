# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.subset = set()
        def dfs(node):
            if node:
                self.subset.add(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        
        for val in self.subset:
            if k-val in self.subset and k-val!=val:
                return True
        return False