class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        LEN = len(nums)
        all_set = []
        def dfs(past, ind):
            if ind>=LEN:
                return
            arr_set = set(past)
            if past:
                # print ("ADD PAST", past, ind)
                all_set.append(past)
            for i in range(ind+1, LEN):
                if nums[i]-k not in arr_set and nums[i]+k not in arr_set:
                    dfs(past+[nums[i]], i)

        for i in range(LEN):
            dfs([nums[i]], i)
        # print (all_set)
        return len(all_set)