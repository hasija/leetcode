class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        val = Counter(nums)
        for i,j in val.items():
            if j>1:
                return i
                    