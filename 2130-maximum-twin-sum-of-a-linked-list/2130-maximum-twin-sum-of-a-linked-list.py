# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        list_l = 0
        node = head
        while node:
            list_l+=1
            node = node.next
        
        node = head
        count = 0
        half_l = list_l//2
        arr = []
        max_v = 0 
        # print ("This is half", half_l)
        while node:
            # print (count)
            if count==half_l:
                max_v = max(arr.pop(-1)+node.val,max_v)
            else:
                count+=1
                arr.append(node.val)
            
            node = node.next
        return max_v
                
                