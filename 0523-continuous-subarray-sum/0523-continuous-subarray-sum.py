class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count = 0
        n = len(nums)
        hash_map = {0:-1}
        count=0
        for start in range(n):
            # print (start)
            count+= nums[start]
            mod_val = count%k
            if mod_val in hash_map:
                if(start-hash_map[mod_val])>1:
                    return True
            else:
                hash_map[mod_val]=start
            # print (hash_map)
        return False
            
            