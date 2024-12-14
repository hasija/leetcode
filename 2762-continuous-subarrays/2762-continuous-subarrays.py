class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        min_ = []
        max_ = []
        l = r = 0
        while r<n:
            # print("start at", r)
            curr = nums[r]
            if not min_:
                # print("empty pass")
                heapq.heappush(min_, (curr, r))
                heapq.heappush(max_, (-curr, r))
                ans += 1
                r+=1
            elif 0<=abs(min_[0][0]-curr)<=2 and 0<=abs(-max_[0][0]-curr)<=2:
                # print("safe pass", r-l+1)
                ans+= r-l+1
                heapq.heappush(min_, (curr, r))
                heapq.heappush(max_, (-curr,r))
                r+=1
            else:
                # print("dropped")
                l+=1
                while max_ and max_[0][1]<l:
                    heapq.heappop(max_)
                while min_ and min_[0][1]<l:
                    heapq.heappop(min_)

        return ans
                