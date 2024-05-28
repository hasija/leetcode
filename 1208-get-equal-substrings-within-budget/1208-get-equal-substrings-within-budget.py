class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        last_ind = 0
        e = len(s)-1
        MAX = 0
        local = 0
        while l<=e:
            # print ("looping============>",l)
            if s[l]==t[l]:
                # print ("similar l")
                local+=1
                l+=1
            else:
                
                diff = abs(ord(s[l])-ord(t[l]))
                # print("diff found", "Max cost left", maxCost, 'diff left', diff)
                if diff<=maxCost:
                    # print ("diff is less, moving l forward")
                    l+=1
                    local+=1
                    maxCost-=diff
                else:
                    # print ("diff is more, push last_ind forward")
                    while last_ind<l and diff>maxCost:
                        # print ("inside else")
                        last_diff = abs(ord(s[last_ind])-ord(t[last_ind]))
                        maxCost+=last_diff
                        last_ind+=1
                        local-=1
                    # print ("last_ind", last_ind, "Maxcost", maxCost)
                    if diff>maxCost:
                        l +=1
                        last_ind = l
                        local = 0
                    else:
                        l+=1
                        local += 1
                        maxCost-=diff
            # print ("local finally", local)
            MAX = max(local, MAX)
            
        return MAX