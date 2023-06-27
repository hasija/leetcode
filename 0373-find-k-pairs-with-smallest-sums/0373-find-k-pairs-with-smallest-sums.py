class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        visited = set()
        arr = []
        pairs = []
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        
        arr.append((nums1[0]+nums2[0],(nums1[0],nums2[0]),(i,j)))
        visited.add((i,j))
        while k>0 and arr:
            val = heapq.heappop(arr)
            pairs.append(val[1])
            i,j=val[2]
            if i+1 <m and (i+1,j) not in visited:
                to_add = (nums1[i+1]+nums2[j],(nums1[i+1],nums2[j]), (i+1,j))
                heapq.heappush(arr, to_add)
                visited.add((i+1,j))
            if j+1<n and (i,j+1) not in visited:
                to_add = (nums1[i]+nums2[j+1],(nums1[i],nums2[j+1]), (i, j+1))
                heapq.heappush(arr, to_add)
                visited.add((i,j+1))
            k-=1
        return pairs
        
            
        