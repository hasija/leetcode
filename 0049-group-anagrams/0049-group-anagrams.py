class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            groups[tuple(sorted(i))].append(i)
        return list(groups.values())