import copy
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        final_arr=[]
        def find_sum(curr_arr, final_val, arr_len):
            # print (curr_arr)
            output = []
            if sum(curr_arr)>final_val:
                return []
            elif sum(curr_arr)==final_val and arr_len == len(curr_arr):
                return curr_arr
            elif len(curr_arr)<arr_len:
                for x in range(curr_arr[-1]-1,0,-1):
                    if x not in curr_arr:
                        tmp_arr = copy.deepcopy(curr_arr)
                        tmp_arr.append(x)
                        output = find_sum(tmp_arr, final_val, arr_len)
                        if len(output)>0:
                            final_arr.append(output)
                            output = []
                    else:
                        continue
            return output
                
                
            
        
        new_out = []
        highest_num = 9
        while highest_num>=2:
            curr_arr = []
            total_sum = highest_num
            out_arr = find_sum([highest_num], n, k)
            if len(out_arr)>1:
                out_arr = set(out_arr)
                if out_arr not in final_arr:
                    final_arr.append(out_arr)
            highest_num-=1
        for val in final_arr:
            new_out.append(list(val))
        # print (final_arr)
        return new_out