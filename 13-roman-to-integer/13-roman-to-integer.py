class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IX":9,
            "IV":4,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        
        unq_set = set(["X","C","I"])
        
        skip = False
        total=0
        for ind in range(len(s)):
            if skip:
                skip=False
                continue
            curr = s[ind]
            if curr in unq_set and ind<len(s)-1 and curr+s[ind+1] in rom_dict:
                skip=True
                total+=rom_dict[curr+s[ind+1]]
            else:
                total+=rom_dict[curr]
        return total
        
        