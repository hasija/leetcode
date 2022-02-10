"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            queue = [root]
        else:
            return []
        out = []
        while (queue!=[]):
            out.append(queue[0].val)
            curr_root = queue[0]
            queue.pop(0)
            if curr_root.children:
                if isinstance(curr_root.children, list):
                    for child in reversed(curr_root.children):
                        queue.insert(0,child)
                else:
                    queue.insert(0,curr_root.children)
                    # print (curr_root.children.val)
                    break
            else:
                continue
        return out
                
                    