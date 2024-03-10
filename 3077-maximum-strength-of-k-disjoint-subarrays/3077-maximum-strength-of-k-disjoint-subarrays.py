class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        len_ = len(nums)
        memo = [ [[-1]*2 for j in range(k+1)] for i in range(len_)]
        
        
        def dp(i,cnt, new_):

            # print ('start',i ,cnt)
            if cnt<=0:
                return 0
            if i>=len_:
                return -float('inf')
            if memo[i][cnt][new_]!=-1:
                return memo[i][cnt][new_]
            curr = nums[i]*cnt
            if cnt%2==0:
                curr*=-1
                
            out = -float('inf')
            # 0 is continue, 1 is new/break sub-arr
            if new_:
                out = max(curr+dp(i+1, cnt, 0), curr+dp(i+1, cnt-1, 1), dp(i+1, cnt, 1))
            else:
                out = max(curr+dp(i+1, cnt, 0), curr+dp(i+1, cnt-1, 1))
            
            memo[i][cnt][new_] = out
            return out
        out =  dp(0,k, 1)
        # print (memo)
        return out
        
            
            
            
                