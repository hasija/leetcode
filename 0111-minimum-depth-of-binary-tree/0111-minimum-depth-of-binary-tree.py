# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            arr = [root]
        else:
            return 0
        count=1
        while arr:
            new_arr =[]
            for node in arr:
                if not node.left and not node.right:
                    return count
                else:
                    if node.left:
                        new_arr.append(node.left)
                    if node.right:
                        new_arr.append(node.right)
            if new_arr:
                arr = new_arr
                count+=1
        return count