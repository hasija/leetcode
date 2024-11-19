class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sub_len = 0
        sub_map = {}
        sub_sum = 0
        n = len(nums)
        ans = 0
        start_idx = 0
        for idx in range(n):
            curr = nums[idx]
            sub_sum+=curr
            if curr in sub_map:
                prev_idx = sub_map[curr]
                while prev_idx>=start_idx:
                    sub_sum-=nums[start_idx]
                    start_idx+=1
                    sub_len-=1
            sub_len+=1
            sub_map[curr]=idx
            if sub_len>k:
                sub_len-=1
                sub_sum-=nums[start_idx]
                sub_map.pop(nums[start_idx])
                start_idx+=1
            if sub_len==k:
                ans = max(ans, sub_sum)
        return ans