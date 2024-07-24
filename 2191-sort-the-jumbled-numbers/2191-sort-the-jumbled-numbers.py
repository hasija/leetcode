class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        hmap = {}
        for idx,val in enumerate(nums):
            new_val = ""
            for i in str(val):
                new_val += str(mapping[int(i)])
            hmap[val]=[int(new_val),idx]
        return sorted(nums, key=lambda x: (hmap[x][0],hmap[x][1]))
        