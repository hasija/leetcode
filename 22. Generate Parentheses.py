class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final_out = []
        def find_complete(temp_str):
            ind_list = []
            stack = []
            for i in range(len(list(temp_str))):
                if i == 0:
                    ind_list.append(i)
                if temp_str[i]=='(':
                    stack.append(temp_str[i])
                if temp_str[i]==')':
                    stack.pop(-1)
                if len(stack)==0:
                    ind_list.append(i)
            return ind_list
        def recurse_comb(value):
            if value==1:
                return ["()"]
            else:
                out_set = set()
                prev_val = recurse_comb(value-1)
                for x in range(len(prev_val)):
                    ind_list = find_complete(prev_val[x])
                    for ind in range(len(ind_list)):
                        if ind == len(ind_list)-1:
                            tmp = prev_val[x]+"()"
                            out_set.add(tmp)
                            continue
                        if ind==0:
                            out_set.add("("+prev_val[x]+")")
                            tmp = "("+prev_val[x][ind_list[ind]:ind_list[ind+1]+1]+")"+prev_val[x][ind_list[ind+1]+1:]
                            out_set.add(tmp)
                            continue
                        tmp = prev_val[x][:ind_list[ind]+1]+"("+prev_val[x][ind_list[ind]+1:ind_list[ind+1]+1]+")"+prev_val[x][ind_list[ind+1]+1:]
                        out_set.add(tmp)
                        tmp = prev_val[x][:ind_list[ind]+1]+"("+prev_val[x][ind_list[ind]+1:]+")"
                        out_set.add(tmp)
                return list(out_set)
        
                            
        final = recurse_comb(n)
        return final
