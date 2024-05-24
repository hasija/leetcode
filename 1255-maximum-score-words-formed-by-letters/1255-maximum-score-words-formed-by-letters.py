class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        let_cnt = Counter(letters)
        word_score = []
        for w in words:
            w_map = Counter(w)
            local_sum = 0
            for i,j in w_map.items():
                if i in let_cnt and j <= let_cnt[i]:
                    ind = ord(i)-97
                    local_sum +=(score[ind]*j)
                else:
                    break
            else:
                word_score.append((w_map, local_sum))
        LEN = len(word_score)
        # print ("word score", word_score)
        def dp(ind, h_map):
            if ind>=LEN:
                return 0
            
            curr_w, curr_s = word_score[ind]
            h_map_copy = h_map.copy()
            flag = False
            # print ("this is current word", curr_w, curr_s)
            for i,j in curr_w.items():
                if h_map[i]>=j:
                    h_map[i]-=j
                else:
                    h_map = h_map_copy
                    # print ("in else", 'Hmap',h_map, 'i,j',i,j)
                    break
            else:
                
                flag = True
            
            if flag:
                # print ("inside flag going for curr_s")
                dp1 = dp(ind+1, h_map.copy())+curr_s
            else:
                dp1 = 0
            
            dp2 = dp(ind+1, h_map_copy.copy())
            
            return max(dp1, dp2)
            
        
        return dp(0, let_cnt)
    
    
    
    
    
    
    
    
    
    
    