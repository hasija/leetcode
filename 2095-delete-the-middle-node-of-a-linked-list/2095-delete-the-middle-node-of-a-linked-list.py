# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        count = 0
        while (node):
            count+=1
            node=node.next
        middle = count//2
        count=0
        prev=None
        # print (middle)
        node = head
        while (node):
            # print (count, middle)
            if count==middle:
                if prev==None:
                    return None
                prev.next=node.next
                break
            else:
                count+=1
                prev=node
                node=node.next
        return head
            
        