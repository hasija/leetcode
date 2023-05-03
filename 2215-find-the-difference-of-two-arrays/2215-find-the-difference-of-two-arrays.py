class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums2 = set(nums2)
        n1 = set(nums1)

        for i in nums1:
            if i not in nums2:
                pass
            else:
                nums2.remove(i)
                n1.remove(i)
        # print ([list(n1),list(nums2)])
        return [list(n1),list(nums2)]
        
                
