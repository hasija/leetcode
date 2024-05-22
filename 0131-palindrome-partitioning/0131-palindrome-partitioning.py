class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.memo = {}
        def check_palindrome(chars):
            if chars in self.memo:
                return self.memo[chars] 
            self.memo[chars] = chars == chars[::-1]
            return self.memo[chars]
            
            
        
        
        def check_palin(arr):
            ans = []
            print ("All pals", arr)
            for pal_arr in arr:
                for pal in pal_arr:
                    if check_palindrome(pal):
                        # ans.append(pal)
                        pass
                    else:
                        break
                else:
                    ans.append(pal_arr)
            return ans
        
        
        def dfs(past, ind):
            if ind>=len(s):
                self.ans = check_palin(past)
                return

            if past:
                
                for arr_ind in range(len(past)):
                    arr = past[arr_ind]
                    
                    new = arr.copy()
                    new[-1]+=s[ind]
                    past.append(new)
                    
                    
                    arr.append(s[ind])
            else:
                past.append([s[ind]])

            
            dfs(past, ind+1)
        dfs([], 0)
        return self.ans
