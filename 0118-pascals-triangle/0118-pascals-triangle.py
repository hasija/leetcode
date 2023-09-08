class Solution:
    def generate(self, n: int) -> List[List[int]]:
        out = []
        for i in range(n):
            arr = []
            for j in range(i+1):
                if j==0 or j==i:
                    arr.append(1)
                else:
                    arr.append(prev[j]+prev[j-1])
            out.append(arr)
            prev = arr.copy()
        
        return out