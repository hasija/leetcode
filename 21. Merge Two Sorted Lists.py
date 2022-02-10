# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add_node(self, l3, val):
        head = l3
        if l3 is None:
            l3 = ListNode(val=val)
            return l3
        while l3.next is not None:
            l3 = l3.next
        l3.next=ListNode(val=val)
        return head
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=None
        curr_node1=l1
        curr_node2=l2
        smaller_node=None
        while True:
            
            if curr_node2:
                print (curr_node2)
                print ("value2")
            if curr_node1:
                print (curr_node1)
                print ("value1")
            if curr_node2 and (curr_node1 is None or curr_node2.val<=curr_node1.val):
                print ("inside if")
                smaller_node=2
                l3=self.add_node(l3,curr_node2.val)
            elif curr_node1:
                print ("inside elif")
                smaller_node=1
                l3=self.add_node(l3,curr_node1.val)
            else:
                print ("inside else")
            print (l3)
            if curr_node2 is None and curr_node1 is None:
                break
            if curr_node1 and smaller_node==1:
                curr_node1 = curr_node1.next

            if curr_node2 and smaller_node==2:
                curr_node2 = curr_node2.next
        return l3