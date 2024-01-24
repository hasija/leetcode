# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        def dfs(node, seen):
            if node:
                if node.val in seen:
                    seen.remove(node.val)
                else:
                    seen.add(node.val)
                dfs(node.right, seen.copy())
                dfs(node.left, seen.copy())
                
                if node.left is None and node.right is None:
                    if len(seen)<=1:
                        self.cnt+=1
                
        dfs(root, set())
        return self.cnt