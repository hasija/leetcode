# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        memo = {}
        # print (root1, root2)
        
        def dfs(n1, n2):
            if (n1, n2) in memo:
                return memo[(n1, n2)]
            if n1 is None and n2 is None:
                memo[(n1, n2)] = True
                return True
            if n1 is None or n2 is None:
                memo[(n1, n2)] = False
                return False
            if n1.val != n2.val:
                memo[(n1, n2)] = False
                return False
            
            ans = None
            if dfs(n1.left, n2.right) and dfs(n1.right, n2.left):
                ans = True
            elif dfs(n1.left, n2.left) and dfs(n1.right, n2.right):
                ans = True
            else:
                ans = False
            memo[(n1, n2)] = ans
            return ans
                
        return dfs(root1, root2)
        