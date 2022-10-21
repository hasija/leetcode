class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count_dict = collections.defaultdict(list)
        for ind in range(len(nums)):
            curr = nums[ind]
            count_dict[curr].append(ind)
            if len(count_dict[curr])>1 and abs(count_dict[curr][-2]-count_dict[curr][-1])<=k:
                return True
        return False
                
            
        