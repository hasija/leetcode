class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        arr = [0]*k
        n = len(cookies)
        
        if n == k:
            return max(cookies)
        
        
        def dfs(i, curr_arr):
            if i==n:
                return max(curr_arr)
            
            val = cookies[i]
            new_arr = []
            for j in range(k):
                curr_arr[j]+=val
                new_arr.append(dfs(i+1, curr_arr))
                curr_arr[j]-=val
            
            return min(new_arr)
        return dfs(0,arr)
                
                