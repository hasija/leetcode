class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ttl = sum(skill)
        teams = len(skill)
        teams //=2 
        target = ttl/teams
        if target != int(target):
            return -1
        
        hmap = defaultdict(int)

        ans = 0
        cnt = 0
        for i in skill:
            to_find = target-i
            if hmap[to_find]>0:
                hmap[to_find]-=1
                ans+=(to_find*i)
                cnt+=1
            else:
                hmap[i]+=1
        if cnt == teams:
            return int(ans)
        else:
            return -1
            