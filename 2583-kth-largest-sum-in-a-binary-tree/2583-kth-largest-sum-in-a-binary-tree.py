# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        bfs = [root]
        lvls = []
        while bfs:
            nxt_lvl = []
            curr_sum = 0
            for node in bfs:
                curr_sum+=node.val
                if node.left:
                    nxt_lvl.append(node.left)
                if node.right:
                    nxt_lvl.append(node.right)
            lvls.append(curr_sum)
            if nxt_lvl:
                bfs = nxt_lvl
            else:
                break
        lvls.sort()
        if len(lvls)<k:
            return -1
        return lvls[-k]