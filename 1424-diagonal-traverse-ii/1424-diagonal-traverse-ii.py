class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        r = len(nums)
        sum_map = defaultdict(list)
        max_c = 0
        for i in range(r):
            max_c = max(max_c, len(nums[i]))
            for j in range(len(nums[i])):
                sum_map[i+j].append(nums[i][j])
        return [j for i in range(r+max_c-1) for j in reversed(sum_map[i])]