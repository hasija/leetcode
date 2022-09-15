class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2!=0:
            return []
        
        changed = sorted(changed)
        count_dict = collections.Counter(changed)
        skip_dict = collections.defaultdict(int)
        ret = []
        count = 0
        while count<n and len(ret)!=(n//2):
            val = changed[count]
            # print (val)
            count+=1
            d = val*2
            if val in skip_dict and skip_dict[val]>0:
                # print ("skip")
                skip_dict[val]-=1
                continue
            if d in count_dict and count_dict[d]>0:
                # print ("double found")
                if d == 0:
                    if (count<n and changed[count]!=0) or (count>=n):
                        return []
                skip_dict[d]+=1
                ret.append(val)
                count_dict[val]-=1
                count_dict[d]-=1
                continue
            elif d in count_dict and count_dict[d]<=0:
                # print ("double but no count left")
                return []
            elif d not in count_dict:
                # print ("double missing")
                return []
        
        if len(ret)!=n//2:
            return []
        return ret