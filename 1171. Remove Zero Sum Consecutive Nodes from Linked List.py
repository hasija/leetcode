# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_arr = []
        start_head = head
        while head:
            list_arr.append(head.val)
            head = head.next
        sum_dict = {}
        sum_dict_set = []
        combination = {}
        sum_val = 0
        final_arr = list_arr.copy()
        bais = 0
        for x in range(len(list_arr)):
            # print (list_arr[x],'start')
            sum_val+= list_arr[x]
            # print (sum_val, sum_dict)
            if list_arr[x]==0:
                continue
            if sum_val == 0:
                final_arr = final_arr[x+1-bais:]
                sum_dict = {}
                sum_dict_set = []
                bais = x+1
                combination = {}
            elif sum_val not in sum_dict:
                sum_dict[sum_val] = x-bais
            elif sum_val in sum_dict:
                initial_ind = sum_dict[sum_val]
                sum_dict_set.append([initial_ind,x-bais])
                if sum_val in combination:
                    combination[sum_val].append(x-bais)
                else:
                    combination[sum_val]= [initial_ind, x-bais]
            # print ('end', final_arr)
        # print ('end', final_arr)
        
        # Removal of value
        # print (sum_dict,'removal start', sum_dict_set)
        iterated_set = []
        
        new_sum_set = []
        # print ('combination', combination)
        for key,val in combination.items():
            for ind1, v1 in enumerate(val):
                for ind2, v2 in enumerate(val[ind1+1:]):
                    # print (v1,v2)
                    new_sum_set.append([v1,v2])
                    
        # print (new_sum_set, 'new sum set')
        
        sum_dict_set = new_sum_set
        diff_arr = [abs(y-x) for x,y in sum_dict_set]
        
        new_set = []
        
        while diff_arr:
            
            index_val = diff_arr.index(max(diff_arr))
            initial_ind, x = sum_dict_set[index_val]
            run = True
            for start,end in iterated_set:
                if start<=initial_ind and end>=initial_ind or start<=x and end>=x:
                    run=False
                    break
            if run:
                iterated_set.append([initial_ind, x])
                new_set.append(sum_dict_set[index_val])
            
            del diff_arr[index_val]
            del sum_dict_set[index_val]
        
        
        # print (new_set)
        new_set.sort()
        
        sum_dict_set = new_set
        iterated_set = []
        # print (final_arr)
        for initial_ind, x in reversed(sum_dict_set):
            # print (initial_ind, x, 'removal')
            final_arr = final_arr[:initial_ind+1] + final_arr[x+1:]
            # print (final_arr)
            
        # print ('final',final_arr)
        # Create linked list
        run_head = start_head
        last_node = run_head
        final_arr = [val for val in final_arr if val!=0]
        if final_arr==[]:
            start_head = None
            return None
        for val in final_arr:
            run_head.val = val
            last_node = run_head
            run_head = run_head.next
        last_node.next=None
        return start_head
            
                
        
        
            