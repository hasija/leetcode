class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        s = arr[0]
        diff = arr[1]-arr[0]
        prev = arr[1]
        for i in range(2, len(arr)):
            new = arr[i]
            if diff != new-prev:
                return False
            prev = new
        return True
        