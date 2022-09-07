# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if node:
                tmp_str = ""+str(node.val)
                left_str = dfs(node.left)
                right_str = dfs(node.right)
                if left_str == right_str == "":
                    return tmp_str
                else:
                    tmp_str += "("+left_str+")"
                    if right_str!="":
                        tmp_str += "("+right_str+")"
                    return tmp_str
            else:
                return ""
        return dfs(root)