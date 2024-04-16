# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        head = root
        arr = [head]
        count = 1
        if depth ==1:
            return TreeNode(val=val,left=root)
        while arr:
            tmp = []
            count+=1
            if count == depth:
                for node in arr:
                    node.left = TreeNode(val=val, left=node.left)
                    node.right = TreeNode(val=val, right=node.right)
                    
                return root
            for node in arr:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            arr = tmp.copy()
        