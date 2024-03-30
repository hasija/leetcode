class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        start = 0
        at_most = 0
        for ind, i in enumerate(nums):
            cnt[i]+=1
            cnt_key = len(cnt.keys())
            if cnt_key<=k:
                at_most+=ind-start+1
            else:
                while cnt_key>k:
                    new_key = nums[start]
                    cnt[new_key]-=1
                    start+=1
                    # print (start, cnt[new_key])
                    if cnt[new_key]==0:
                        cnt.pop(new_key)
                        at_most += ind-start+1
                        # print (i-start+1, i, start, cnt)
                        break


        start = 0
        cnt = defaultdict(int)
        k -=1 
        at_most_less = 0
        for ind, i in enumerate(nums):
            cnt[i]+=1
            cnt_key = len(cnt.keys())
            if cnt_key<=k:
                at_most_less+=ind-start+1
            else:
                while cnt_key>k:
                    new_key = nums[start]
                    cnt[new_key]-=1
                    start+=1
                    if cnt[new_key]==0:
                        cnt.pop(new_key)
                        at_most_less += ind-start+1
                        break


        
        
        return at_most-at_most_less
                    
        