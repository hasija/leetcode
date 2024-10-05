class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        map_s1 = Counter(s1)
        map_s2 = defaultdict(int)
        cnt = 0
        # print ("this is s1", map_s1)
        def check_map(m1, m2):
            # print (m1, m2)
            for k,v in m1.items():
                if v!=m2[k]:
                    return False
            return True
        
        for i in range(n2):
            # print ("curr idx", i)
            cnt += 1
            curr = s2[i]
            
            if cnt>n1:
                last_idx = i-n1
                last_val = s2[last_idx]
                map_s2[last_val]-=1
            map_s2[curr]+=1
            # print ("curr map of s2", map_s2)
            if check_map(map_s1, map_s2):
                return True
            else:
                pass
        return False
                
                
            