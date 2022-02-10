from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_set = []
        final_list = []
        tmp_hash=set()
        def check_in_list(val):
            return_set = []
            tmp = dict(Counter(val))
            for sets in hash_set:
                if tmp==sets:
                    return tmp
            return None
        
        for y in range(len(strs)):
            flag=False
            old_set = hash_set
            old_set = check_in_list(strs[y])
            if old_set is None:
                tmp_hash = dict(Counter(strs[y]))
                hash_set.append(tmp_hash)
                final_list.append([strs[y]])
            else:
                index = hash_set.index(old_set)
                final_list[index].append(strs[y])
        return final_list