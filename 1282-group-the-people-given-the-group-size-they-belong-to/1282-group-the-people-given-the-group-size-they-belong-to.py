class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        h_map = defaultdict(list)
        for ind, val in enumerate(groupSizes):
            h_map[val].append(ind)
        # print (h_map)
        out = []
        for k,v in h_map.items():
            tmp = []
            for ind in v:
                tmp.append(ind)
                if len(tmp) == k:
                    out.append(tmp)
                    tmp=[]
            # print (out, k)
        return out