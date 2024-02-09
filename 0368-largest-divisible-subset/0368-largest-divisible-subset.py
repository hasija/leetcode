class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        memo = {}
        nums.sort()
        memo_dict = {i:ind for ind,i in enumerate(nums)}
        memo_list = list(memo_dict.keys())
        def dp(i):
            if i in memo:
                return memo[i]
            ind = memo_dict[i]
            curr = []
            curr_len = 0
            flag = False
            for j in range(0, ind):
                prev_num = memo_list[j]
                if i%prev_num !=0:
                    continue
                dp_out = dp(prev_num)
                if dp_out[0]>curr_len:
                    curr_len = dp_out[0]
                    curr = dp_out[1].copy()
                    flag = True
            
            if flag:
                curr_len+=1
                curr.append(i)
            else:
                curr_len = 1
                curr = [i]
            memo[i] = [curr_len, curr]
            return memo[i]
        max_ = None
        max_len = 0
        for i in nums:
            len_, curr = dp(i)
            if len_>max_len:
                max_ = curr
                max_len = len_
        return max_
        
            
                
            
        
     