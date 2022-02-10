class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        output_num = 0
        for x in range(0, len(s)-1):
            if roman_dict[s[x]]>= roman_dict[s[x+1]]:
                output_num += roman_dict[s[x]]
            else:
                output_num -= roman_dict[s[x]]
                
        return output_num+roman_dict[s[len(s)-1]]