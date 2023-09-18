class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for ind, i in enumerate(mat):
            arr.append((sum(i),ind))
        
        arr = sorted(arr, key=lambda x: (x[0], x[1]))
        print(arr)
        return [i[1] for i in arr[:k]]
        
            