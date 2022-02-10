# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        start = boost = head
        start_set = set()
        while (start):
            if start not in start_set:
                start_set.add(start)
            else:
                return start
            start = start.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        start = boost = head
        if not head:
            return None
        while(True):

            if start.next and boost.next and boost.next.next:
                start = start.next
                boost = boost.next.next
            else:
                return None
            if start==boost:
                break
        print (head.val, start.val)
        while (head!=start):
            # print ("inloop")
            # print (head.val, start.val)
            head=head.next
            start = start.next
        return start


# algo:
'''
P and q are starting point p travels twice as fast
dist by q at meeting point with p => m+k where m is distance to start point and k is distance from loop start point to point of meet
dist by p => m+k+l where l is loops of cycle 
so 2q = p as p was travelling two times the speed of q
hence ==> m+k+l = 2m + 2k => m+k=l
so m more steps will take us to the loop start.
'''