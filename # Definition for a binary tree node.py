# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        old_root = root
        self.change_hands(root)
        return old_root
    def change_hands(self,root):
        if root:
            tmp=root.left
            root.left=root.right
            root.right=tmp
            self.change_hands(root.left)
            self.change_hands(root.right)
    def traversal(self,root):
        if root:
            print (root.val)
            self.traversal(root.left)
            self.traversal(root.right)

    def change_hands(self,root):
        if root:
            root.left,root.right=self.change_hands(root.right),self.change_hands(root.left)

