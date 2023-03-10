# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head        

    def getRandom(self) -> int:
        seats = 1
        sample_space = 1
        selected = None
        head = self.head
        while head:
            if random.random()<seats/sample_space:
                selected = head.val
            head = head.next
            sample_space+=1
        return selected
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()