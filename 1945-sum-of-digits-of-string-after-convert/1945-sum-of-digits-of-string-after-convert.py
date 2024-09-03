class Solution:
    def getLucky(self, s: str, k: int) -> int:
        vals = ""
        for i in s:
            vals+=str(ord(i)-96)
        for i in range(k):
            new_vals = 0
            for j in vals:
                new_vals+=int(j)
            vals = str(new_vals)
        return int(vals)