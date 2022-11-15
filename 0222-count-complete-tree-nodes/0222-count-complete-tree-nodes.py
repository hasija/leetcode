# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        node_arr = [root]
        count = 0
        while node_arr:
            tmp_arr = []
            for node in node_arr:
                if node:
                    count+=1
                    if node.left:
                        tmp_arr.append(node.left)
                    if node.right:
                        tmp_arr.append(node.right)
            node_arr = tmp_arr
        return count
                
            