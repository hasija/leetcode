# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        def traverse(node, parent, last_move, left_max, right_max):
            if self.flag is False:
                return
            if node:
                # print (node.val, left_max, right_max)
                if last_move=='left':
                    if (parent and node.val>=parent.val) or node.val <=left_max or node.val>=right_max:
                        self.flag=False
                        # print (node.val, left_max, right_max)
                        return
                elif last_move=='right':
                    if (parent and node.val<=parent.val) or node.val <=left_max or node.val>=right_max:
                        self.flag=False
                        # print (node.val, left_max, right_max)
                        return
                
                
                traverse(node.left, node, 'left', left_max, min(right_max, node.val) )
                traverse(node.right, node, 'right', max(left_max, node.val), right_max)
        traverse(root.left, root, 'left', float('-inf'), root.val)
        traverse(root.right, root, 'right', root.val , float('inf'))
        return self.flag