class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        t_ind = 0
        for i in s:
            curr_t = t[t_ind]
            if curr_t==i:
                t_ind+=1
                if t_ind>=len(t):
                    return 0
        return len(t)-t_ind
            