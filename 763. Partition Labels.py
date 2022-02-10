class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ind_dict={}
        start_ind = 0
        end_ind = 0
        tmp_dict={}
        final_arr=[]
        re_start=True
        
        def check_within(tmp_dict, final_ind):
            max_val = final_ind
            # find all within
            checked_set=set()
            check_set = set()
            while True:
                for val in tmp_dict:
                    if val not in checked_set:
                        if min(tmp_dict[val])<max_val:
                            check_set.add(val)
                # print (check_set, max_val)
                if len(check_set)==0:
                    return max_val
                # max_val
                for val in check_set:
                    if max(tmp_dict[val])>max_val:
                        max_val = max(tmp_dict[val])
                    checked_set.add(val)
                check_set=set()
            # for val in tmp_dict:
            #     if min(tmp_dict[val])<=final_ind and max(tmp_dict[val])>max_val:
            #         max_val = max(tmp_dict[val])
            # return max_val
                    
        
        while end_ind<=len(s):
            # print (start_ind, end_ind)
            if end_ind==len(s):
                if s[start_ind]==s[end_ind-1]:
                    final_arr.append(end_ind-start_ind)
                    end_ind+=1
                    continue
                else:
                    min_val = min(tmp_dict[s[end_ind-1]])
                if min_val < ind_dict[s[start_ind]] or start_ind==end_ind-1:
                    final_arr.append(end_ind-start_ind)
                    end_ind+=1
                    continue
                else:
                    new_ind = check_within(tmp_dict, ind_dict[s[start_ind]])
                    final_arr.append(new_ind-start_ind+1)
                    start_ind = new_ind+1
                    re_start = True
                    end_ind = new_ind+1
                    continue
            if re_start:
                ind_dict[s[end_ind]]=end_ind
                end_ind+=1
                re_start=False
                continue
            if s[end_ind] in ind_dict:
                ind_dict[s[end_ind]]=end_ind
                end_ind+=1
                continue
            elif s[end_ind] in tmp_dict:
                tmp_dict[s[end_ind]].append(end_ind)
                end_ind+=1
                continue
            else:
                tmp_dict[s[end_ind]]=[end_ind]
                end_ind+=1
                continue
        return final_arr