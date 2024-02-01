class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        tmp = []
        ans = []
        last = None
        print(nums)
        for i in nums:
            tmp.append(i)
            if last and abs(last-i)>k:
                return []
            if len(tmp)==3:
                ans.append(tmp)
                tmp = []
                last = None
            else:
                last = tmp[0]
        return ans
                