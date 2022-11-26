class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp_end = [0]
        dp_prof = [0]
        
        def search(dp, e):
            # print (dp, e, 'search')
            l = 0
            r = len(dp)-1
            while l<=r:
                mid = (l+r)//2
                

                if dp[mid]<=e:
                    if l==r:
                        return l
                    l=mid+1
                else:
                    if l==r:
                        return l-1
                    r=mid-1
            # print ("found", min(l,r))
            out = min(l,r)
            return out
            if dp[out]>e:
                return out-1
            else:
                return out
        
        def bSearch( dp, target):
            left, right = 0, len(dp)

            while left < right:
                mid = (left + right)//2

                if dp[mid] <= target:
                    left = mid + 1
                else:
                    right = mid

            return left


        for s,e,p in arr:
            # idx = bSearch(dp_end, s)
            idx = search(dp_end, s)
            # print (idx)
            curr_prof = dp_prof[idx]+p
            if curr_prof>dp_prof[-1]:
                dp_prof.append(curr_prof)
            else:
                dp_prof.append(dp_prof[-1])
            dp_end.append(e)
            # print (s,e, p, idx,dp_prof[-1])
        print (dp_prof)
        return dp_prof[-1]
        
        
        