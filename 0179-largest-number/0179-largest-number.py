class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        l = 0
        r = n-1
        def msort(l,r):
            if l>=r:
                return [str(nums[r])]
            if (r-l+1)>=2:
                mid = (l+r)//2
                left = msort(l, mid)
                right = msort(mid+1, r)
            
            final = []
            l_idx, r_idx = 0,0
            # print ('left and right', left, right)
            for i in range(r-l+1):
                while l_idx<len(left) and r_idx<len(right):
                    left_val = str(left[l_idx])
                    right_val = str(right[r_idx])
                    if left_val+right_val>right_val+left_val:        
                        final.append(left_val)
                        l_idx+=1
                    else:
                        final.append(right_val)
                        r_idx+=1
                while l_idx<len(left):
                    final.append(str(left[l_idx]))
                    l_idx+=1
                while r_idx<len(right):
                    final.append(str(right[r_idx]))
                    r_idx+=1
            # print ("Val returned", final)
            return final
        
        out =  ''.join(msort(l,r))
        if out[0]=='0':
            return '0'
        else:
            return out
            
            
            