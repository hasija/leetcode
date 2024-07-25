class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):

            if len(arr)>1:
                l = 0
                r = len(arr)-1
                mid = (l+r)//2

                arr_left = merge_sort(arr[l:mid+1].copy())
                arr_right = merge_sort(arr[mid+1:r+1].copy())
                ans = []
                i=j=0
                while i<len(arr_left) or j<len(arr_right):
                    left = float('inf')
                    right = float('inf')
                    if i<len(arr_left):
                        left = arr_left[i]
                    if j<len(arr_right):
                        right = arr_right[j]
                    
                    if left<right:
                        ans.append(left)
                        i+=1
                    else:
                        ans.append(right)
                        j+=1
                return ans
            else:
                return arr
        return merge_sort(nums)