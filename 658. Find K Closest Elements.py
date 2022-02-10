class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start_ind = x
        # left = start_ind-1
        # right = start_ind+1
        final_arr=[]
        left = 0
        right = len(arr)-1
        def binar_search(val, left, right):
            if left>right:
                return left,right
            mid = (left+right)//2
            # print ('bs',mid, left, right)
            if arr[mid]==val:
                return mid,None
            elif arr[mid]<val:
                left=mid+1
                return binar_search(val, left, right)
            elif arr[mid]>val:
                right=mid-1
                return binar_search(val, left, right)
        
                
        mid,status = binar_search(x, left,right)
        if status==None:
            # print ("here")
            left = mid
            right = mid
        else:
            left = mid
            right = status
            if left==len(arr):
                left-=1
            if right<0:
                right=0
            if left>right:
                left,right=right,left
        
        def get_value(left, right, start_ind, k):
            # print (left, right)
            if left>=0:
                left_val = abs(arr[left]-start_ind)
            else:
                left_val = float('inf')
            if right<len(arr):
                right_val = abs(arr[right]-start_ind)
            else:
                right_val = float('inf')
            if right_val>left_val:
                final_arr.append(arr[left])
                left-=1
            elif left_val>right_val:
                final_arr.append(arr[right])
                right+=1
            elif left_val==right_val and left_val!=float('inf') and arr[left]<arr[right]:
                final_arr.append(arr[left])
                left-=1
            elif left_val==right_val and left_val!=float('inf') and arr[left]==arr[right]:
                if left==right:
                    right+=1
                final_arr.append(arr[left])
                left-=1
            if k>1:
                k-=1
                if left_val==right_val==float('inf'):
                    k=0
                    return
                get_value(left, right, start_ind, k)
        get_value(left, right, start_ind, k)
        final_arr.sort()
        return final_arr