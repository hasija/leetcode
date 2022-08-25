class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        base = collections.Counter(ransomNote)
        max_dict = collections.Counter(magazine)
        
        for k,v in base.items():
            if k in max_dict and max_dict[k]>=v:
                continue
            else:
                return False
        return True
        