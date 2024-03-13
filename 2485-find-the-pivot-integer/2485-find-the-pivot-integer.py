class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_arr = [0]
        prefix = 0
        for i in range(1, n+1):
            prefix+=i
            sum_arr.append(prefix)
        
        for ind in range(1,n+1):
            curr = sum_arr[ind]
            final = sum_arr[n]-curr+ind
            if final == curr:
                return ind
        return -1
            
            
            