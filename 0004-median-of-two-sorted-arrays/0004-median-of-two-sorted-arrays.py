class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        t = n+m
        if t%2==0:
            median = [t//2-1, t//2]
        else:
            median = [t//2]
        final = t//2+1
        p1 = p2 = 0
        cnt = 0
        ans = []
        while median:
            
            n1 = nums1[p1] if p1<n else +float('inf')
            n2 = nums2[p2] if p2<m else +float('inf')
            if n1<=n2:
                if cnt==median[0]:
                    median.pop(0)
                    ans.append(n1)
                p1+=1
                cnt+=1
            else:
                if cnt==median[0]:
                    median.pop(0)
                    ans.append(n2)
                p2+=1
                cnt+=1
        
        if len(ans)>1:
            return sum(ans)/2
        else:
            return ans[0]