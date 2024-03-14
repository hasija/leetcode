class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ones = sum(nums)
        zeros = deque()
        zero = 0
        cnt=0
        post = 0
        ans = 0
        
        def count_sub(val):
            prev = 0
            for ind in (range(val)):
                prev += ind+1
            return prev
                
        
        if goal == 0 :
            prev = 0
            prev_ind = 0
            for ind, i in enumerate(nums):
                if i ==0:
                    prev += prev_ind+1
                    prev_ind+=1
                else:
                    ans+=prev
                    prev = 0
                    prev_ind = 0
            ans+=prev
            return ans

        first_flag = False
        prev_pre_ = 0
        for ind, i in enumerate(nums):
            
            if i ==1:
                zeros.append(zero)
                zero = 0
                if cnt!=goal:
                    cnt+=1
                    
                    
                if cnt == goal:
                    
                    ans+=1
                    # print ('zeros',zeros, zero)
                    if zeros:
                        pre_=deque.popleft(zeros)
                    else:
                        pre_=0
                    if first_flag :
                        post_ = zeros[-1]
                    else:
                        first_flag = True
                        post_ = 0
                    
                    ans+=prev_pre_*post_
                    ans+=pre_
                    ans+=post_
                    prev_pre_ = pre_
            else:
                zero+=1
            # print (ind, i, ans)
        # look for post first
        if cnt==goal:
            ans+=zero
            ans+=pre_*zero
            
        return ans
            
                