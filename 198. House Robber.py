class Solution:
    def rob(self, nums: List[int]) -> int:
        sum_arr=[]
        for x in range(len(nums)):
            if x>=2:
                sum_arr.append(nums[x]+max(sum_arr[:-1]))
            else:
                sum_arr.append(nums[x])
        return max(sum_arr)
            