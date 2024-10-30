class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis_left = []
        len_from_left = []
        lis_right = []
        len_from_right = []
        for i in nums:
            idx = bisect.bisect_left(lis_left, i)
            if idx<len(lis_left):
                lis_left[idx] = i
            else:
                lis_left.append(i)
            len_from_left.append(idx+1)
        
        
        for i in reversed(nums):
            idx = bisect.bisect_left(lis_right, i)
            if idx<len(lis_right):
                lis_right[idx] = i
            else:
                lis_right.append(i)
            len_from_right.append(idx+1)
        # print (len_from_left, len_from_right)
        reversed_right_len = list(reversed(len_from_right))
        max_idx = None
        max_cnt = 0
        for idx in range(1,len(nums)-1):
            curr_cnt = reversed_right_len[idx]+len_from_left[idx]
            if max_cnt<curr_cnt and len_from_left[idx]!=1 and reversed_right_len[idx]!=1:
                max_cnt = curr_cnt
                max_idx = idx
        # print ("max val", max_cnt, max_idx)
        # removing the extra count
        max_cnt -=1
        return len(nums)-max_cnt
        
        
            
        
        
        
        