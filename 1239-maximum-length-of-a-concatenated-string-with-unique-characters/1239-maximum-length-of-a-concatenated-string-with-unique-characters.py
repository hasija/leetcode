class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for val in arr:
            val_set = set(val)
            if len(val_set)<len(val):
                continue
            for old_val in dp:
                if (old_val&val_set):
                    continue
                else:
                    dp.append(old_val|val_set)
        return max([len(val) for val in dp])
        