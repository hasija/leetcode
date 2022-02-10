from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        start_ind = 0
        end_ind = 0
        max_len = 0
        option = 'right'
        while end_ind<len(nums):
            # print (start_ind, end_ind, 'start')
            if option=='right':
                while max_deque and max_deque[-1]<nums[end_ind]:
                    max_deque.pop()
                max_deque.append(nums[end_ind])
                while min_deque and min_deque[-1]>nums[end_ind]:
                    min_deque.pop()
                min_deque.append(nums[end_ind])
            # print (max_deque[0], min_deque[0], 'deque')
            if max_deque[0]-min_deque[0]<=limit:
                # print ('right')
                max_len = max(max_len, end_ind-start_ind+1)
                option = 'right'
                end_ind+=1
            else:
                # print ('left')
                option='left'
                if nums[start_ind]==max_deque[0]:
                    max_deque.popleft()
                if nums[start_ind]==min_deque[0]:
                    min_deque.popleft()
                start_ind+=1
        return max_len
        
        
