class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        new_dict = collections.defaultdict(list)
        for val in strs:
            new_dict[tuple(sorted(val))].append(val)
        return new_dict.values()
        