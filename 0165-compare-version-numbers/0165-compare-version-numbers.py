class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        len1 = len(v1)
        len2 = len(v2)
        for i in range(max(len1, len2)):
            try:
                r1 = int(v1[i])
            except:
                r1 = 0
            try:
                r2 = int(v2[i])
            except:
                r2 = 0
            if r1>r2:
                return 1
            elif r2>r1:
                return -1
        return 0
        