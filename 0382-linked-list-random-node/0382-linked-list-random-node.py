# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.new_arr = []
        while head:
            self.new_arr.append(head.val)
            head=head.next
        

    def getRandom(self) -> int:
        t = len(self.new_arr)
        ind = random.randint(0, t-1)
        return self.new_arr[ind]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()