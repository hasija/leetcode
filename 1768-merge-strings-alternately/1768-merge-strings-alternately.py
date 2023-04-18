class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""
        for i,j in zip(word1, word2):
            new_str+=i+j
        n = len(word1)
        m = len(word2)
        if n==m:
            return new_str
        else:
            if n>m:
                new_str+=word1[m:]
            else:
                new_str+=word2[n:]
        return new_str