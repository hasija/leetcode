# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hash_m = {v:i for i, v in enumerate(inorder)}
        
        r = len(inorder)-1
        def recurse(l, r):
            # print (l,r)
            if l>r:return None
            root = postorder.pop()
            node = TreeNode(val=root)
            node.right = recurse(hash_m[root]+1, r)
            node.left = recurse(l,hash_m[root]-1)
            return node
        return recurse(0, r)
            
        
            