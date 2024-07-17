# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.nodes_to_delete = []
        to_delete = set(to_delete)
        def dfs(node, parent, move):
            if node:
                if node.val in to_delete:
                    self.nodes_to_delete.append((node, parent,move))
                
                dfs(node.left, node,'left')
                dfs(node.right, node, 'right')
        
        dfs(root, None, None)
        
        final_nodes = [root]
        ans = []
        def delete_node(node, parent, move):
            if parent:
                if move == 'left':
                    parent.left = None
                else:
                    parent.right = None
            if node.left:
                final_nodes.append(node.left)
            if node.right:
                final_nodes.append(node.right)
            node.left = None
            node.right = None
        
        for i in self.nodes_to_delete:
            delete_node(i[0], i[1], i[2])
        
        for i in final_nodes:
            if i.val not in to_delete:
                ans.append(i)
        return ans
            
                
                
                    