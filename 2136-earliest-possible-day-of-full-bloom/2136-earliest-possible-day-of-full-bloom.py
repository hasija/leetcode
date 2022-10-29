class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        index = sorted(range(len(growTime)), key= lambda x: -growTime[x])
        res = 0
        plant_t = 0
        for val in index:
            plant_t+=plantTime[val]
            res = max(plant_t+growTime[val], res)
        return res