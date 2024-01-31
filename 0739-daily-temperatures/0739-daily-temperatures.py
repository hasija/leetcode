class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        seen = defaultdict(list)
        
        for ind, tmp in enumerate(temperatures):
            if not seen:
                seen[tmp].append(ind)
                min_tmp = tmp
            if tmp>min_tmp:
                min_tmp = float('inf')
                items_to_pop = []
                for old_tmp, ind_list in seen.items():
                    if old_tmp<tmp:
                        for old_ind in ind_list:
                            temperatures[old_ind]=ind-old_ind
                        items_to_pop.append(old_tmp)
                [seen.pop(item) for item in items_to_pop]
                    
                min_tmp = tmp
            seen[tmp].append(ind)
            min_tmp = min(min_tmp, tmp)
        for i,j in seen.items():
            for k in j:
                temperatures[k]=0 
        return temperatures
                