class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(l,r):
            if l>r:
                return -1
            mid = (l+r)//2
            print (l,r,mid)
            if nums[mid]==target:
                return mid
            if target>nums[mid]:
                return bsearch(mid+1, r)
            else:
                return bsearch(l,mid-1)
        return bsearch(0, len(nums)-1)