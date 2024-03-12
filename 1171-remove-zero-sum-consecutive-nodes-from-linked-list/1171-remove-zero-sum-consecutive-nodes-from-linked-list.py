# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        start = dummy
        prefix = 0
        track = {}
        while start:
            prefix += start.val
            if prefix not in track:
                track[prefix] = start
                start = start.next
            else:
                prev = track[prefix]
                prev_base = prev
                prev = prev.next
                p = prefix+prev.val
                # print ("all track", track.keys(), 'curr', start.val, 'curr_sum', prefix)
                while p!=prefix:
                    # print ("DELETING", p)
                    prev = prev.next
                    del track[p]
                    p += prev.val
                track[prefix] = prev_base
                prev_base.next = prev.next
                start = prev.next
        return dummy.next
                
                
                
                