class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        all_prime_nums = []
        
        def is_prime(val):
            for i in range(2, int(sqrt(val))+1):
                if val%i==0:
                    return False
            return True
        
        for val in range(2, max(nums)):
            if is_prime(val):
                all_prime_nums.append(val)
        n = len(all_prime_nums)
        last = 0
        ans = []
        # print("all prime nums", all_prime_nums)
        for i in nums:
            idx = bisect.bisect_left(all_prime_nums, i)
            if idx>=n:
                idx-=1
            elif idx+1<n and all_prime_nums[idx+1]!=i:
                idx-=1
            new_val = None
            # print ("check for i", i, "idx found", idx, 'last val', last)
            while idx>=0 and i-all_prime_nums[idx]<=last:
                idx-=1
            if idx<0 and i<=last:
                return False
            elif idx>=0:
                last = i-all_prime_nums[idx]
            else:
                last = i
        return True