class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = collections.defaultdict(int)
        for val in arr:
            cnt[val]+=1
        
        new_set = set()
        for k,v in cnt.items():
            if v in new_set:
                return False
            else:
                new_set.add(v)
        return True