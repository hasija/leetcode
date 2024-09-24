class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        h_set = set()
        for num in arr1:
            curr = str(num)
            tmp = ""
            for i in curr:
                tmp+=i
                h_set.add(tmp)
        ans = 0
        for num in arr2:
            curr = str(num)
            n = len(curr)
            tmp = ""
            for i in range(n):
                tmp+=curr[i]
                if tmp in h_set:
                    ans = max(ans, i+1)
                else:
                    break
        return ans