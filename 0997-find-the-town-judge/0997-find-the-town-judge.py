class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt = defaultdict(set)
        t_arr = [0 for i in range(n+1)]
        if n==1 and len(trust)==0:
            return 1
        for i,j in trust:
            cnt[j].add(i)
            t_arr[i]+=1
        
        for i,j in cnt.items():
            if len(j)==n-1 and t_arr[i]==0:
                return i
        return -1