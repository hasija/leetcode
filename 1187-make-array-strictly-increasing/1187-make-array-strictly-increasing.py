class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
        memo = {}
        arr2.sort()
        def dfs(prev, i):
            if (prev, i) in memo:
                return memo[(prev, i)]
            
            if len(arr1)==i:
                return 0
            
            cost = float('inf')
            
            if arr1[i]>prev:
                cost = dfs(arr1[i], i+1)
            
            small_idx = bisect.bisect_right(arr2, prev)
            
            if small_idx<len(arr2):
                cost = min(cost, 1+dfs(arr2[small_idx], i+1))
                
            memo[(prev, i)] = cost
            return cost
        
        res = dfs(-1, 0)
        return -1 if res==float('inf') else res