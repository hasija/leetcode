class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        sort_arr = sorted(properties, key=lambda x: (x[0],x[1]))
        new_arr = []
        prev = None
        for val in sort_arr:
            if val[0]==prev:
                new_arr[-1][-1].append(val[1])
            else:
                new_arr.append([val[0],[val[1]]])
            prev = val[0]
        final_count = 0
        max_def = float('-inf')
        for weak in range(len(new_arr)-2,-1,-1):
            # for strong in range(weak+1, weak, -1):
            strong = weak+1
            weak_att = new_arr[weak][0]
            count = []
            strong_def = new_arr[strong][1][-1]
            min_def = new_arr[weak][1][0]
            if strong_def>max_def:
                max_def=strong_def
            for defence_ind in reversed(range(len(new_arr[weak][1]))):
                defence = new_arr[weak][1][defence_ind]
                if defence<max_def:
                    count.append(defence_ind)
                    # new_arr[weak][1].pop(defence_ind)
            # count.sort(reverse=True)
            # for val in count:
            #     new_arr[weak][1].pop(val)
            final_count+=len(count)
            # if new_arr[weak][1]==[]:
            #     break
        return final_count
        