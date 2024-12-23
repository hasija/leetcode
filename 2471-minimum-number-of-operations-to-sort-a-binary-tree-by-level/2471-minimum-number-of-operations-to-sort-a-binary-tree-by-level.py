# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        arr = [root]
        ans = 0
        
        
        def sort_arr(vals, idx_map):
            sorted_arr = sorted(vals)
            n = len(vals)
            cnt = 0
            for idx in range(n):
                if sorted_arr[idx] == vals[idx]:
                    continue
                else:
                    cnt+=1
                    correct_val = sorted_arr[idx]
                    new_idx = idx_map[correct_val]
                    incorrect_val = vals[idx] 
                    vals[new_idx] = vals[idx] 
                    vals[idx] = correct_val
                    idx_map[incorrect_val] = new_idx
            return cnt
        
        while arr:
            next_arr = []
            vals_arr = []
            idx_map = {}
            idx = 0
            for node in arr:
                if node.left:
                    next_arr.append(node.left)
                    vals_arr.append(node.left.val)
                    idx_map[node.left.val]=idx
                    idx+=1
                if node.right:
                    next_arr.append(node.right)
                    vals_arr.append(node.right.val)
                    idx_map[node.right.val]=idx
                    idx+=1
            
            if next_arr:
                items_sorted=sort_arr(vals_arr, idx_map)
                # print("count at current level", items_sorted)
                ans+=items_sorted
                arr = next_arr
            else:
                break
        return ans
            