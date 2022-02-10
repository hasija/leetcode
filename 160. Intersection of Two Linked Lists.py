class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        old_arr_a=set()
        old_arr_b=set()
        while True:
            if headA:
                old_arr_a.add(headA)
            if headB:
                old_arr_b.add(headB)
            if headB in old_arr_a:
                return headB
            elif headB:
                headB=headB.next
            if headA in old_arr_b:
                return headA
            elif headA:
                headA=headA.next
            if headA is None and headB is None:
                return None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        old_headB=headB
        old_headA=headA
        count1=0
        count2=0
        while True:
            if headA:
                headA=headA.next
                count1+=1
            else:
                break
        while True:
            if headB:
                headB=headB.next
                count2+=1
            else:
                break
        headA=old_headA
        headB=old_headB
        if count1!=count2:
            for x in range(abs(count1-count2)):
                if count1>count2:
                    headA=headA.next
                else:
                    headB=headB.next
        while True:
            if headA and headB and headA==headB:
                return headA
            elif headA and headB:
                headA=headA.next
                headB=headB.next
            else:
                return None