# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        arr = [[-1]*n for i in range(m)]
        move = ['right','bot','left','up']
        curr_move = 0
        curr_posi = [0,-1]
        
        def get_posi(posi, curr_move):
            if move[curr_move] == 'right':
                return posi[0],posi[1]+1
            if move[curr_move] == 'bot':
                return posi[0]+1,posi[1]
            if move[curr_move] == 'left':
                return posi[0],posi[1]-1
            if move[curr_move] == 'up':
                return posi[0]-1,posi[1]
            
        
        while head:
            
            val = head.val
            r,c = get_posi(curr_posi, curr_move)
            # print ('val',val, 'posi', r,c,'move',curr_move)
            if 0<=r<m and 0<=c<n and arr[r][c]==-1:
                arr[r][c]=val
                head=head.next
                curr_posi = [r,c]
            else:
                curr_move+=1
                curr_move%=4
                
                
        return arr
            