# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        LEN = distance+1
        self.ans = 0
        def dfs(node):
            if node:
                l = dfs(node.left)
                r = dfs(node.right)
                arr = [0]*LEN
                if l is None and r is None:
                    arr[0]=1
                    return arr
                for i in range(1, LEN):
                    l_val = r_val = 0
                    if l:
                        l_val = l[i-1]
                    if r:
                        r_val = r[i-1]
                    arr[i]=l_val+r_val
                if l and r:
                    # print ('curr node',node.val,"arr, both found", arr, l, r)
                    for i in range(LEN):
                        for j in range(LEN):
                            if l[i] and r[j] and i+j+2<=distance:
                                self.ans+=(l[i]*r[j])
                    # print("Ans after cal", self.ans)
                return arr
            else:
                return None
        arr = dfs(root)
        # print (arr)
        return self.ans