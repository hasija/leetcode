class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        out = 0
        for letter in letters:
            i = s.index(letter)
            j = s.rindex(letter)
            if i!=j:
                out+=len(set(s[i+1:j]))
        return out
            
        