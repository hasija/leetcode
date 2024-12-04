class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)
        m = len(str2)
        def dfs(start_idx, check_idx):
            if check_idx>=m:
                return True
            if start_idx>=n:
                return False
            if n-start_idx<m-check_idx:
                return False
            check_char = str2[check_idx]
            for idx in range(start_idx, n):
                next_char = ord(str1[idx])-97
                next_char +=1
                next_char %= 26
                next_char += 97
                next_char = chr(next_char)
                if str1[idx] == check_char or check_char==next_char:
                    if dfs(idx+1, check_idx+1):
                        return True
            return False
        for idx in range(0, n):
            if n-idx < m:
                return False
            if dfs(0, 0):
                return True
        return False