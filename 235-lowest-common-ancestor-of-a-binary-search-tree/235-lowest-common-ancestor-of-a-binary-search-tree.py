# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.out=None
        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                if node.val == p.val or node.val ==q.val:
                    mid = True
                else:
                    mid=False
                count = 0
                if mid:
                    count+=1
                if left:
                    count+=1
                if right:
                    count+=1
                # print (node.val, count)
                if count>=2:
                    self.out = node
                if count>=1:
                    return True
                else:
                    return False
        dfs(root)
        return self.out
                    