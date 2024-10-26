# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        max_val_map = defaultdict(int)
        height_map = defaultdict(int)
        
        
        def get_height(node):
            if node:
                if node.val in height_map:
                    return height_map[node.val]
                curr = 1+max(get_height(node.left), get_height(node.right))
                height_map[node.val]=curr
                return curr
            else: 
                return 0
            

        def dfs(node, depth, max_val):
            if node:
                # print ("node iter", node.val, depth, max_val)
                max_val_map[node.val] = max_val
                right_depth = get_height(node.right)
                left_depth = get_height(node.left)

                    
                dfs(node.left, depth+1, max(max_val, depth+right_depth))
                dfs(node.right, depth+1, max(max_val,depth+left_depth))
        
        dfs(root, 0, 0)
        # print (max_val_map)
        return [max_val_map[q] for q in queries]
            
                
                