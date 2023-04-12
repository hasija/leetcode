class Solution:
    def simplifyPath(self, path: str) -> str:
        final_arr = []
        # to store value
        tmp_string = ""
        path += '/'
        n = len(path)
        # print (path)
        prev_slash = 0
        for i in range(n):
            curr_val = path[i]
            # print (i, curr_val)
            # condition one, to get values between two slashes
            if curr_val =='/':
                # print(prev_slash, 'prev slash')
                # print(i , 'curr_slash')
                # print (tmp_string, path[prev_slash+1:i], 'new entries between slashes')
                # print (final_arr)
                # condition 2nd
                if tmp_string =='..':
                    if len(final_arr)>0:
                        final_arr.pop()
                # Condition 3rd single dot
                elif tmp_string == '.':
                    pass
                else:
                    if len(tmp_string)>0:
                        final_arr.append(tmp_string)
                
                tmp_string = ""
                # operations are done
                prev_slash = i
            else:
                tmp_string+=curr_val
        
        final_str = "/"
        
        arr_len = len(final_arr)
        # arr_len: 2
        # ind 0 , 1 --> final_ind 1 ==2-1
        
        for ind in range(arr_len):
            # last value
            val = final_arr[ind]
            if ind == arr_len-1:
                final_str+=val
            else:
                final_str+=val+'/'
        return final_str
                
        
        
            
            
            