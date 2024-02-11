class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        all_ = Counter("".join(words))
        ans = 0
        word_len = sorted([len(i) for i in words])
        even = odd = 0
        for _,w in all_.items():
            if w%2==1:
                odd+=1
                w-=1
            even+=w
        ans = 0
        for cnt, w in enumerate(word_len):
            print ("word_len",w, "even",even,"odd", odd)
            if w%2==1:
                if odd ==0:
                    even-=1
                    odd+=2
                odd-=1
                w-=1
            if (w>0 and even>=w) or w==0:
                even-=w
                ans+=1
            else:
                break
        return ans
            
            
                
                
            
                    
        
        
        
        
        
        
        
        
                    