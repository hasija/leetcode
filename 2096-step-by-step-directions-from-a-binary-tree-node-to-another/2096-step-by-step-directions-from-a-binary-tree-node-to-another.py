# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        self.find2 = False
        val_to_find = None
        def dfs2(node, move):
            if node:
                if self.find2:
                    return ""
                if node.val==val_to_find:
                    self.find2=True
                    return move
                val1 = dfs2(node.left, 'L')
                val2 = dfs2(node.right, 'R')
                if self.find2:
                    return move+val1+val2
                else:
                    return ""
            else:
                return ""
        
        val_to_find = startValue
        v1 = dfs2(root, '')
        val_to_find = destValue
        self.find2 = False
        v2 = dfs2(root, '')
        cnt = 0
        LEN = min(len(v1),len(v2) )
        for i in range(LEN):
            if v1[i]==v2[i]:
                cnt+=1
            else:
                break
        return 'U'*len(v1[cnt:])+v2[cnt:]
                    