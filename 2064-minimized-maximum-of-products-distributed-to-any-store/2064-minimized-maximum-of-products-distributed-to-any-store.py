class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        def divide_product(val):
            start = 0
            to_divide = quantities[start]
            for i in range(n):
                if to_divide<=val:
                    start+=1
                    if start == m:
                        return True
                    else:
                        to_divide = quantities[start]
                else:
                    to_divide -= val
            return False
        
        left = 0
        right = max(quantities)
        ans = None
        while left<=right:
            mid = (left+right)//2
            if divide_product(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans