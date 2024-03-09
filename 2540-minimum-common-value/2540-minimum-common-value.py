class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = 0
        p2 = 0
        while p1<len(nums1) and p2<len(nums2):
            c1 = nums1[p1]
            c2 = nums2[p2]
            if c1 == c2:
                return c1
            if c1>c2:
                p2+=1
            else:
                p1+=1
        return -1