# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output=[]
        queue = []
        queue = [root]
        def recurse(queue, tmp, next_queue):            
            while(len(queue)>0):
                node = queue[0]
                tmp.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                queue.pop(0)
            output.append(tmp)
            tmp=[]
            if len(next_queue)>0:
                queue = next_queue
                next_queue = []
                recurse(queue, [], [])
            else: return
        if root:
            recurse(queue, [], [])
        return output