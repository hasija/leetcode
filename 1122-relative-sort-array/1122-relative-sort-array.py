class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        ans = []
        for i in arr2:
            ans.extend([i]*cnt[i])
            cnt.pop(i)
        rem = sorted(cnt.keys())
        for i in rem:
            ans.extend([i]*cnt[i])
        return ans