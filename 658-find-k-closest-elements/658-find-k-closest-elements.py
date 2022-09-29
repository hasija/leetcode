class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def b_search(arr, x):
            l = 0
            r = len(arr)-1
            while l<=r:
                mid = (l+r)//2
                if arr[mid] == x:
                    return mid, min(mid+1, len(arr)-1)
                
                if arr[mid]>x:
                    r=mid-1
                else:
                    l=mid+1
            return max(0, min(l,r)), min(len(arr)-1, max(l,r))
        l,r=b_search(arr,x)
        if l==r:
            r+=1
        # print (l,r)
        
        out = collections.deque()
        while len(out)<k:
            # print (out, l, r)
            if l>=0:
                left = abs(arr[l]-x)
            else:
                left = None
            if r<len(arr):
                right = abs(arr[r]-x)
            else:
                right = None
            # print ("run", left, right)
            if left is not None and right is not None:
                if left<=right:
                    out.appendleft(arr[l])
                    l-=1
                else:
                    out.append(arr[r])
                    r+=1
            elif right is not None:
                out.append(arr[r])
                r+=1
            elif left is not None:
                out.appendleft(arr[l])
                l-=1
            if left is None and right is None:
                return None
        
        return out
            
                
                