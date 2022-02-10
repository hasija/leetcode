class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[]
        
        def dfs(arr, tree):
            if len(arr)==0:
                output.append(tree)
            for i in range(len(arr)):
                dfs(arr[:i]+arr[i+1:], tree+[arr[i]])
        dfs(nums,[])
        return output