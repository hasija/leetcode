class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        arr_by_cnt = []

        def get_cnt(val):
            val = bin(val)[2:]
            cnt = 0
            for i in val:
                if i =='1':
                    cnt+=1
            return cnt

        for i in nums:
            arr_by_cnt.append(get_cnt(i))

        n = len(nums)
        ans = []
        for i in range(n):
            if i == 0:
                last_idx = 0
                last = arr_by_cnt[i]
                continue
            if last == arr_by_cnt[i]:
                pass
            else:
                tmp_arr = nums[last_idx: i]
                # print (last_idx, tmp_arr)
                tmp_arr.sort()
                ans += tmp_arr
                last = arr_by_cnt[i]
                last_idx = i
        tmp_arr = nums[last_idx:n]
        tmp_arr.sort()
        ans+=tmp_arr
        # print (ans, sorted(nums))
        return ans == sorted(nums)
                