# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                # print ("def left, rught", left, rught)
                coins = left+right+node.val-1
                self.moves += abs(left)+abs(right)
                return coins
            else:
                return 0
        dfs(root)
        return self.moves