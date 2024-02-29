# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        arr = [root]
        is_even = True 
        last = -float('inf')
        while arr:
            tmp = []
            for node in arr:
                if is_even and node.val%2==0:
                    return False
                if not is_even and node.val%2!=0:
                    return False
                if is_even and last>=node.val:
                    return False
                if not is_even and last<=node.val:
                    return False
                last = node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            arr = tmp
            is_even = not is_even
            last = -float('inf')
            if not is_even:
                last *= -1
        return True
                
                
                    