class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum([1 for w in words if len(set(w).difference(allowed))==0])