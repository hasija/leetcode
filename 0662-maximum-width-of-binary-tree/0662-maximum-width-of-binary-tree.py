# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        arr = [(1,root)]
        self.max = 1
        while arr:
            new_arr = []
            l_flag = False
            count = 0
            start_ind = None
            end_ind = None
            new_found = False
            
            for idx, node_arr in enumerate(arr):
                counter = 1
                ind, node = node_arr
                buffer = (ind-1)*2
                # print ("iterating arr", idx, node.val)
                if node.left:
                    new_arr.append((counter+buffer,node.left))
                    counter+=1
                else:
                    counter+=1
                   
                if node.right:
                    new_arr.append( (counter+buffer, node.right))
                    counter+=1
                    new_found=True
                else:
                    counter+=1

                if start_ind is None:
                    start_ind=ind
                end_ind = ind
            
            if start_ind is not None:
                curr_val = end_ind-start_ind+1
                self.max = max(self.max, curr_val)
                # print("end of loop, start, end, val, max", start_ind, end_ind, curr_val, self.max)
                arr = new_arr
        return self.max