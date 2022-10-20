class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1:["I","V"], 2:["X","L"], 3:["C","D"], 4:["M","N"]}
        
        num_str = str(num)
        n = len(num_str)
        out = []
        for ind in range(len(num_str)):
            curr_ind = n-ind
            curr_val = int(num_str[ind])
            if curr_val<4:
                local = roman_dict[curr_ind][0]
                out.append(local*curr_val)
                continue
            if curr_val>=5 and curr_val<9:
                local = roman_dict[curr_ind][1]
                out.append(local)
                new_val=curr_val-5
                local = roman_dict[curr_ind][0]
                out.append(local*new_val)
                continue
            if curr_val==4:
                local = roman_dict[curr_ind]
                out.extend([local[0],local[1]])
                continue
            if curr_val==9:
                local = roman_dict[curr_ind]
                local_next = roman_dict[curr_ind+1]
                out.extend([local[0], local_next[0]])
        return "".join(out)
            
        