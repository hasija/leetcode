class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        p1 = 0
        p2 = 0
        n = len(nums)
        bits = [0]*30
        
        def count_bits(val, ops):
            val = bin(val)[2:][::-1]
            for idx,i in enumerate(val):
                if i=='1' and ops=='add':
                    bits[idx]+=1
                elif i=='1' and ops=='sub':
                    bits[idx]-=1
            ret_num = ""
            for i in bits:
                ret_num+= '1'if i>0 else '0'
            return int(ret_num[::-1],2)
    
    
        ans = float('inf')
        while p2<n:
            ret_val = count_bits(nums[p2],'add')
            # print ('ret val and and ret val',ret_val&k,ret_val)
            while ret_val>=k and p1<=p2:
                ans = min(ans, p2-p1+1)
                ret_val = count_bits(nums[p1],'sub')
                p1+=1
            p2+=1
        return -1 if ans == float('inf') else ans
                
                
            