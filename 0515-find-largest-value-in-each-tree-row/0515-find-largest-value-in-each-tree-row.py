# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        arr = [root]
        if not root:
            return []
        ans = []
        while True:
            max_ = -float('inf')
            nxt_arr = []
            for node in arr:
                max_ = max(node.val,max_)
                if node.left:
                    nxt_arr.append(node.left)
                if node.right:
                    nxt_arr.append(node.right)
            ans.append(max_)
            if not nxt_arr:
                return ans
            arr = nxt_arr
        return ans