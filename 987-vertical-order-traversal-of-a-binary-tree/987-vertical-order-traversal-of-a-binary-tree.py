# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.node_dict = collections.defaultdict(list)
        def dfs(node, row, col):
            if node:
                self.node_dict[(row,col)].append(node.val)
                dfs(node.left, row+1, col-1)
                dfs(node.right, row+1, col+1)
        dfs(root, 0,0)
        # print (self.node_dict)
        
        node_keys = list(self.node_dict.keys())
        node_keys = sorted(node_keys, key = lambda x: (x[1], x[0]))
        out = []
        last_col = None
        for key in node_keys:
            
            if len(self.node_dict[key])<2:
                tmp_arr = self.node_dict[key]
            else:
                tmp_arr = sorted(self.node_dict[key])
            
            # print (last_col, key[1], tmp_arr, out)
            if last_col is not None and last_col==key[1]:
                out[-1].extend(tmp_arr)
            else:
                out.append(tmp_arr)
            last_col = key[1]
        return out

            