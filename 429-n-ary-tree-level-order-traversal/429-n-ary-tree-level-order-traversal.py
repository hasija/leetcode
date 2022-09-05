"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        arr = [root]
        out = []
        if root is None:
            return []
        while arr:
            tmp_arr=[]
            curr_arr=[]
            for node in arr:
                curr_arr.append(node.val)
                for child in node.children:
                    tmp_arr.append(child)
            out.append(curr_arr)
            arr = tmp_arr
        return out
            
        