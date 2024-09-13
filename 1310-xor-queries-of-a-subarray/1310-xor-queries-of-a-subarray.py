class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = []
        
        for i in range(len(arr)):
            if i==0:
                prefix_xor.append(arr[i])
            else:
                prefix_xor.append(prefix_xor[-1]^arr[i])
        
        ans = []
        for i,j in queries:
            if i==0:
                ans.append(prefix_xor[j])
            else:
                ans.append(prefix_xor[j]^prefix_xor[i-1])
        return ans