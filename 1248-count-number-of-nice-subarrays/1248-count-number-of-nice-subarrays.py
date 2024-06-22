class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        prev = None
        odd_queue = deque()
        ans = 0
        for idx, i in enumerate(nums):
            if i%2==1:
                cnt+=1
                odd_queue.appendleft(idx)
            else:
                pass
            
            if cnt>k:
                first = odd_queue.pop()
                last = odd_queue[0]
                if len(odd_queue)>1:
                    second_last = odd_queue[1]
                else:
                    second_last = first
                diff_last = last-second_last
                if prev is None:
                    diff_start = first+1
                else:
                    diff_start = first-prev
                print (diff_start, diff_last)
                ans += diff_start*diff_last
                prev = first
                cnt-=1
        print (ans, "till loop ans")
        if cnt==k:
            first = odd_queue.pop()
            if prev is None:
                diff_start = first+1
            else:
                diff_start = first-prev
            last = len(nums)
            if len(odd_queue)>=1:
                second_last = odd_queue[0]
            else:
                second_last = first
            diff_last = last-second_last
            print (diff_start, diff_last)
            ans += diff_start*diff_last
                
                
            
        return ans
                
                
        