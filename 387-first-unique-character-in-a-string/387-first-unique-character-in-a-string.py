class Solution:
    def firstUniqChar(self, s: str) -> int:
        c_dict = collections.Counter(s)        
        for ind in range(len(s)):
            char = s[ind]
            if c_dict[char]==1:
                return ind
        return -1
        