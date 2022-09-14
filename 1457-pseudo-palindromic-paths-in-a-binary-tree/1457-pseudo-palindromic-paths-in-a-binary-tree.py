# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        node_dict = collections.defaultdict(int)
        self.count = 0
        def dfs(node):
            if node:
                node_dict[node.val]+=1
                out1 , val =dfs(node.left)
                if out1:
                    node_dict[val]-=1
                out2 , val =dfs(node.right)
                if out2:
                    node_dict[val]-=1
                
                if out1 == out2 ==False:
                    tmp = 0
                    for k,v in node_dict.items():
                        if v%2!=0:
                            tmp+=1
                    if tmp<=1:
                        self.count+=1
                return True, node.val
            else:
                return False, -1
        dfs(root)
        return self.count