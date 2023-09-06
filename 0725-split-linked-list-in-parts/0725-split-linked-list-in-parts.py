# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list_l = 0
        s = head
        while s:
            list_l+=1
            s=s.next
        
        mean = list_l//k
        buffer = list_l%k
        # print (mean, buffer)
        arr = []
        s = head
        count = 0
        start = s
        while s:
            # print (s.val)
            count+=1
            if buffer:
                check = mean+1
            else:
                check = mean
            # print ("to be cheked",check, "current", count)
            if count == check:
                arr.append(start)
                start = s.next
                s.next = None
                s=start
                if buffer:
                    buffer-=1
                count=0
            else:
                s=s.next
        while len(arr)!=k:
            arr.append(None)
        return arr
    
    
    