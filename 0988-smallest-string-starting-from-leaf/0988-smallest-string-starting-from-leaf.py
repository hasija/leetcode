# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        h_map = {i:chr(i+97) for i in range(26)}
            
        
        def dfs(node):
            if node:
                curr = h_map[node.val]
                left=dfs(node.left)
                right=dfs(node.right)
                if not left and not right:
                    return [curr]
                left = [n+curr for n in left] 
                right = [n+curr for n in right]
                return left+right
            else:
                return []
        # print (dfs(root))
        return min(dfs(root))