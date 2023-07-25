class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        r= len(arr)-1
        while l<r:
            # print (l,r)
            mid = (l+r)//2
            left = mid-1
            right = mid+1
            # print (left,mid,right)
            if arr[left]<arr[mid]>arr[right]:
                return mid
            elif arr[left]<arr[mid]<arr[right]:
                l =mid
            else:
                r=mid
        return r
            