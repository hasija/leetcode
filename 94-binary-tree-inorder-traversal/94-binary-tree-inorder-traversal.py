# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            arr = collections.deque([root])
        else:
            arr = []
        out = []
        while arr:
            # print (arr[0].val)
            curr = arr[0]
            left_flag = False
            if curr.left:
                left_flag = True
                arr.appendleft(curr.left)
            curr.left=None
            if not left_flag:
                out.append(curr.val)
                arr.popleft()
                if curr.right:
                    arr.appendleft(curr.right)
        # print (out)
        return out
            
                
            
        