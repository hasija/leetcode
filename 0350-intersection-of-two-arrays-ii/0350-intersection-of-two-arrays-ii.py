class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = []
        for i,j in cnt1.items():
            if i in cnt2:
                ans+=[i]*min(j,cnt2[i])
        return ans