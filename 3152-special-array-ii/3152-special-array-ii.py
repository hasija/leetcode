class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        bad_pairs = set()
        last = None
        for idx, i in enumerate(nums):
            if i%2==last:
                bad_pairs.add((idx-1, idx))
            else:
                last = i%2
        # print(arr)
        ans = []
        for i,j in queries:
            flag = False
            for x,y in bad_pairs:
                if i<=x<=j and i<=y<=j:
                    flag = True
                    ans.append(False)
                    break
            if not flag:
                ans.append(True)
        return ans