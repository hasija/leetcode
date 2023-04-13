class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        m = len(popped)
        push_ind = 0
        pop_ind = 0
        
        while pushed and push_ind <len(pushed) and pop_ind<m :
            n = len(pushed)
            if push_ind<n:
                push_val = pushed[push_ind]
            else:
                push_val = None
            pop_val = popped[pop_ind]
            # print (push_val, pop_val, 'looping')
            if push_val == pop_val:
                pop_ind+=1
                pushed.pop(push_ind)
                if push_ind>0:
                    push_ind-=1
            # elif push_ind>0 and pushed[push_ind-1] == pop_val:
            #     pop_ind+=1
            else:
                push_ind+=1
        if pop_ind==m:
            return True
        else:
            return False