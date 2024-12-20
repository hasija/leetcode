# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lvl = True
        arr = [root]
        def attach_node(arr, nodes, lvl):
            for p in arr:
                p.left=nodes.pop()
                p.right=nodes.pop()

            # print("rebuilding")
            # print(p.left.val)
            # print(p.right.val)
            
                
        
        while arr:
            next_lvl = []
            # print ("Looping arr")
            for node in arr:
                if node.left:
                    next_lvl.append(node.left)
                    next_lvl.append(node.right)
                else:
                    break
            if not next_lvl:
                break
            if not lvl:
                new_node = list(reversed(next_lvl))
                # print ("new nodes", new_node)
                attach_node(list(reversed(arr)), new_node, lvl)
            else:
                # print("inside the other lvl")
                attach_node(arr, next_lvl.copy(), lvl)
            lvl = not lvl
            arr = next_lvl
            
        return root
                