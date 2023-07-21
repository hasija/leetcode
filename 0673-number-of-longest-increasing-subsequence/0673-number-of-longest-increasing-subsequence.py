class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        count = [1]*n
        length = [1]*n
        max_len = 1
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    if length[j]+1>length[i]:
                        length[i] = length[j]+1
                        max_len = max(max_len,length[i])
                        count[i]=count[j]
                        
                    elif length[j]+1<length[i]:
                        continue
                    else:
                        count[i]+=count[j]
        total = 0
        for i in range(n):
            if length[i]==max_len:
                total+=count[i]
        return total