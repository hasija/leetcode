class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        arr = [[i]*cnt[i] for i in sorted(cnt.keys(), key=lambda x: (cnt[x], -x))]
        ans = []
        [ans.extend(i) for i in arr]
        return ans