# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        last = None
        first = None
        min_dist = float('inf')
        max_dist = 0
        cnt = 0
        while head.next:
            cnt+=1
            if not prev:
                prev = head
                head=head.next
                continue
            else:
                if (
                    (prev.val<head.val and head.val>head.next.val)
                    or
                    (prev.val>head.val and head.val<head.next.val)):
                        if last:
                            min_dist = min(cnt-last, min_dist)
                        if first:
                            max_dist = cnt-first
                        else:
                            first = cnt
                        last = cnt
            prev = head
            head= head.next
            # print (first, last)
        if max_dist:
            return [min_dist, max_dist]
        else:
            return [-1, -1]