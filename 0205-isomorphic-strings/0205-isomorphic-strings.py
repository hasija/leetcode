class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_t = {}
        used = set()
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            curr= s[i]
            tar = t[i]
            if tar in map_t and map_t[tar]!=curr:
                return False
            elif tar not in map_t and curr not in used:
                map_t[tar] = curr
                used.add(curr)
            elif tar not in map_t and curr in used:
                return False
        return True
                
                
            