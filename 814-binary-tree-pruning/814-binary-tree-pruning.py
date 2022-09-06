# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root_head = TreeNode(val=0, left=root)
        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                if left==0:
                    node.left = None
                if right==0:
                    node.right=None
                return (left+right+node.val)
            else:
                return 0
                    
        dfs(root_head)
        return root_head.left