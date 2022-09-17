class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        pairs = []
        
        def check_palin(new_word):
            rev = new_word[::-1]
            if new_word==rev:
                return True
            else:
                return False
        
        w_dict= {}
        for ind in range(n):
            w = words[ind]
            w_dict[w]=ind
        
        
        for w, ind in w_dict.items():
            # print (w, ind)
            rev = w[::-1]
            if rev in w_dict and w_dict[rev]!=ind:
                # print ("palind is present")
                pairs.append([ind, w_dict[rev]])
            if  w!="" and w==rev and "" in w_dict:
                # print ("blank found")
                pairs.append([ind, w_dict[""]])
                pairs.append([w_dict[""], ind])
            
            for k in range(1, len(w)):
                first_half = w[:k]
                second_half = w[k:]
                if first_half == first_half[::-1] and second_half[::-1] in w_dict:
                    pairs.append([w_dict[second_half[::-1]], ind])
                if second_half == second_half[::-1] and first_half[::-1] in w_dict:
                    pairs.append([ind, w_dict[first_half[::-1]]])
        return pairs
                    
                
            
                
                
        