class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        final = sorted([(i,j) for i,j in cnt.items()], key = lambda x: -x[1])
        s = ""
        for i,j in final:
            s+=i*j
        return s
        
        