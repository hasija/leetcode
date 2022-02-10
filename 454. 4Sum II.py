class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # final_arr = []
        # # recurse on nums1 and recures on list
        # new_arr = [nums1, nums2, nums3, nums4]
        # def recurs(arr_ind, build_arr):
        #     # print (build_arr)
        #     if arr_ind>=len(new_arr):
        #         if sum(build_arr)==0:
        #             # print (build_arr)
        #             final_arr.append(build_arr)
        #             return
        #         else:
        #             return
        #     for ind in range(len(new_arr[arr_ind])):
        #         build_arr.append(new_arr[arr_ind][ind])
        #         recurs(arr_ind+1, build_arr)
        #         build_arr.pop()
        # recurs(0, [])
        # # print (final_arr)
        # return len(final_arr)
        
        count = {}
        final_count = 0
        for a in nums1:
            for b in nums2:
                count[a+b] = count.get(a+b,0)+1
        for c in nums3:
            for d in nums4:
                if (-c-d) in count:
                    final_count+=count[-d-c]
        return (final_count)