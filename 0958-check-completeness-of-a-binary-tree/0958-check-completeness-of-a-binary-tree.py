# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        arr = [root]
        prev = True        
        while arr:
            new_arr = []

            for node in arr:
                if not prev and node.left:
                    return False
                if node.left:
                    new_arr.append(node.left)
                else:
                    prev=False
                if not prev and node.right:
                    return False
                if node.right:
                    new_arr.append(node.right)
                else:
                    prev=False
            arr = new_arr
        return True
                    