# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root and root.left and root.right:
            arr = [(root.left, root.right)]
        elif root and not root.left and not root.right:
            return True
        else:
            return False
        while arr:
            new_arr = []
            for i,j in arr:
                if i.val==j.val:
                    # print (i.val, j.val, 'matched')
                    if i.left and j.right:
                        new_arr.append((i.left,j.right))
                    elif (i.left and not j.right) or (not i.left and j.right):
                        return False
                    
                    if i.right and j.left:
                        new_arr.append((i.right,j.left))
                    elif (j.left and not i.right) or (not j.left and i.right):
                        return False
                else:
                    # print (i.val, j.val)
                    return False
            arr = new_arr
        return True
                    