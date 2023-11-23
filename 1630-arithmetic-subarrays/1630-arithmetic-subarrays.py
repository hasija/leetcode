class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check_arr(arr):
            h_set = set()
            min_v = float('inf')
            max_v = -float('inf')
            for val in arr:
                h_set.add(val)
                max_v = max(max_v, val)
                min_v = min(min_v, val)
            diff = (max_v-min_v)/(len(arr)-1)
            if diff%1!=0:
                return False
            diff = int(diff)
            for i in range(1,len(arr)):
                if min_v+(i*diff) not in h_set:
                    return False
            return True
        
        out = []
        for i,j in zip(l,r):
            out.append(check_arr(nums[i:j+1]))
        return out