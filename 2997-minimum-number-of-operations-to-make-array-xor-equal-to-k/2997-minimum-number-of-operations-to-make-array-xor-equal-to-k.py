class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        past = 0
        for i in nums:
            past = past^i
        # final_xor = bin(past)[2:]
        # target = bin(k)[2:]
        change = k^past
        change = bin(change)[2:]
        ans = 0
        for i in change:
            if i == '1':
                ans+=1
        return ans