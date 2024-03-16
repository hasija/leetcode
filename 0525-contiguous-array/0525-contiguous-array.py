class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {}
        cnt = 0
        max_l = curr_l = 0
        count_map[0] = -1
        for ind,i in enumerate(nums):
            if i == 1:
                cnt+=1
            else:
                cnt-=1
            if cnt not in count_map:
                count_map[cnt]=ind
            else:
                curr_l = ind - count_map[cnt]
                max_l = max(max_l, curr_l)
        return max_l
                