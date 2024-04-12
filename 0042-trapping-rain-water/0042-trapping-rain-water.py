class Solution:
    def trap(self, height: List[int]) -> int:
        left_ind = 0
        right_ind = len(height)-1
        left_max = 0
        right_max = 0
        vol = 0
        if len(height)<3:
            return 0
        
        while left_ind<right_ind:
            left_val = height[left_ind]
            right_val = height[right_ind]
            left_max = max(left_max, left_val)
            right_max = max(right_max, right_val)
            if left_max<=right_max:
                vol += left_max-left_val
                left_ind+=1
            else:
                vol+=right_max-right_val
                right_ind-=1
        return vol
        
        