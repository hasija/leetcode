class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        s1 = Counter(s1)
        s2 = Counter(s2)
        for i,j in s2.items():
            s1[i]+=j
        
        return [k for k,v in s1.items() if v==1]
        