# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        start = ListNode(next=head)
        base = start
        prev = start
        while start:
            if start.val in nums_set:
                prev.next = start.next
                start = start.next
            else:
                prev=start
                start=start.next
        return base.next
        