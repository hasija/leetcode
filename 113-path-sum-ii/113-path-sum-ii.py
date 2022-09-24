# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.total = 0
        out = []
        def dfs(node, total, path):
            if node:
                # print (node.val, path)
                total+=node.val
                path.append(node.val)
                left = dfs(node.left, total, path.copy())
                right = dfs(node.right, total, path.copy())
                if left is None and right is None and total == targetSum:
                    out.append(path)
                return 1
        dfs(root, 0, [])
        return out