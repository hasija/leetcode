class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head= root
        queue  = [root]
        level =[]
        prev = None
        if root:
            while(queue):
                curr = queue[0]
                queue.pop(0)
                if prev:
                    prev.next = curr
                    prev = curr
                else:
                    prev = curr
                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)
                if len(queue)==0 and len(level)>0:
                    prev = None
                    queue = level
                    level = []
        return head
            

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head= root
        prev = None
        left_start =None
        while(root):
            # print (root.val)
            if root.left:
                if not left_start:
                    left_start = root.left
                if prev:
                    # print("Inside rootleft prev")
                    # print (prev.val)
                    prev.next = root.left
                    prev = prev.next
                else:
                    # print("Inside rootleft else")
                    prev = root.left
            if root.right:
                if not left_start:
                    left_start = root.right
                if prev:
                    # print("Inside rootright prev")
                    prev.next = root.right
                    prev = prev.next
                else:
                    # print("Inside rootright else")
                    prev = root.right
            if root.next:
                root =root.next
            elif left_start: 
                root = left_start
                left_start=None
                prev=None
            else:
                return head
        return head
            