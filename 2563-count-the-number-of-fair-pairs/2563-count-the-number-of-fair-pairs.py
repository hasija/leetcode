class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        ans = 0        
        nums.sort()
        
        def find_count(limit):
            left = 0
            right = n-1
            cnt = 0
            for left in range(n-1):
                # print ("looping", left)
                total = nums[left]+nums[right]
                while left<right and total>=limit:
                    # print ("total, limit",total, limit)
                    right-=1
                    total = nums[left]+nums[right]
                # print ("resutlt", left, right)
                if left<right:
                    cnt += right-left
                # print ("cnt", cnt)
            return cnt
        less_than_lower = find_count(lower)
        total_till_upper = find_count(upper+1)
        # print(less_than_lower, total_till_upper)
        # print ("ans", total_till_upper-less_than_lower)
        return  total_till_upper-less_than_lower
                