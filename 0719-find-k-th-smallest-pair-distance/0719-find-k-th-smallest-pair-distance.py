class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1]-nums[0]
        def get_count(val):
            n = len(nums)
            cnt = 0
            j=1
            # max_v = -1
            for i in range(n-1):
                while (j< n and nums[j]-nums[i]<=val):
                    j+=1

                cnt+=j-i-1
            return cnt
        
        def find_k(low, high):
            ans = -1
            while low<=high:
                # print ("low and high start", low, high)
                mid = (high+low)//2
                # print ("mid val", mid)
                cnt = get_count(mid)
                # print ("return from cnt", cnt, mid)
                if cnt>=k:
                    high = mid-1
                    ans=mid
                else:
                    low = mid+1
                # print ("low and high after",low, high)
            return ans
        return find_k(low, high)