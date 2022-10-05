# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth ==1:
            new = TreeNode(val=val, left=root)
            return new
        
        d = 1
        row = [root]
        flag = False
        while row:
            if d == depth-1:
                flag=True
            tmp_row = []
            for node in row:
                if flag:
                    new_node_left = TreeNode(val=val)
                    new_node_right = TreeNode(val=val)
                    node.left, new_node_left.left = new_node_left, node.left
                    node.right, new_node_right.right = new_node_right, node.right
                    
                else:
                    if node.left:
                        tmp_row.append(node.left)
                    if node.right:
                        tmp_row.append(node.right)
            if flag:
                return root
            row = tmp_row
            d+=1
        return root
        