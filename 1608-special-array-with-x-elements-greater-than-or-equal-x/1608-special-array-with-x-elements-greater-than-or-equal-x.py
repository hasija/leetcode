class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        cnt = len(nums)
        
        arr = [0]*(len(nums)+1)
        for i in range(1, cnt+1):
            idx = bisect.bisect_left(nums, i)
            total = len(nums)-idx
            # print ("index", idx, 'num to serach', i)
            # if idx<cnt and nums[idx]!=i:
            #     total+=1
            # print ("total nums greate or equal", total)
            arr[i] = total
            if total==i:
                return i
        return -1
            