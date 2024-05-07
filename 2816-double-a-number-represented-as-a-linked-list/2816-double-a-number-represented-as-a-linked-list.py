# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        node = head
        new_val = 0
        while node:
            # arr.append(str(node.val))
            new_val*=10
            new_val += node.val
            node = node.next
        # print (new_val)
        new_val *= 2
        # new_list = list(str(new_val))
        # print (new_list)
        head = ListNode()
        prev = head
        new_arr = []
        if new_val == 0:
            return head
        while new_val:
            i = new_val%10
            new_val = new_val//10
            new_arr.append(i)
        
        while new_arr:
            i = new_arr.pop()
            new = ListNode(val=i)
            prev.next = new
            prev = new
        
                
                
        
        return head.next