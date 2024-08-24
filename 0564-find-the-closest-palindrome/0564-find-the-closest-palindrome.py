class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def get_half(n):
            LEN = len(n)
            if LEN%2==0:
                return str(n)[:(LEN//2)]
            else:
                return str(n)[:(LEN//2)+1]
        base = get_half(n)
        arr = []
        is_even = False
        if len(n)%2==0:
            is_even=True
        
        if is_even:
            arr.append(int(base+base[::-1]))
            
            one_up = str(int(base)+1)
            arr.append(int(one_up+one_up[::-1]))
            one_down = str(int(base)-1)
            arr.append(int(one_down+one_down[::-1]))
        else:
            second_half = base[:-1][::-1]
            arr.append(int(base+second_half))
            one_up = str(int(base)+1)
            arr.append(int(one_up+one_up[:-1][::-1]))
            one_down = str(int(base)-1)
            arr.append(int(one_down+one_down[:-1][::-1]))
        
        LEN = len(n)
        fourth_val = (10**LEN)+1
        fifth_val = int(('9'*(LEN-1))) if LEN>1 else 9
        arr.append(fourth_val)
        arr.append(fifth_val)
        diff = float('inf')
        ans = None
        n = int(n)
        # print (arr)
        for val in arr:
            if val == n:
                continue
            if abs(n-val)<diff:
                diff = abs(n-val)
                ans = val
            elif abs(n-val)==diff:
                ans = min(ans, val)
        return str(ans)