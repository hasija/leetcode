# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bfs = [(root, None)]
        while bfs:
            new_arr = []
            parent_map = defaultdict(int)
            total = 0
            for node, parent in bfs:
                parent_map[parent] += node.val
                total += node.val
                if node.left:
                    new_arr.append((node.left, node))
                if node.right:
                    new_arr.append((node.right, node))
            
            for node, parent in bfs:
                node.val = total - parent_map[parent]
            if new_arr:
                bfs = new_arr
            else:
                break
        return root