class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for i in logs:
            if i[:2]=='..':
                cnt-=1
                cnt = max(0,cnt)
            elif i[:2]!='./':
                cnt+=1
        return cnt