class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # l = 0
        # r= len(s)-1
        # ind_to_remove = []
        # while(l<r):
        #     if s[l]==s[r]:
        #         print ("here 1")
        #         l+=1
        #         r-=1
        #         continue
        #     else:
        #         if l<=r-1 and s[l]==s[r-1]:
        #             print ("here 2")
        #             ind_to_remove.append(r)
        #             l+=1
        #             r-=2
        #             continue
        #         elif r>=l+1 and s[r]==s[l+1]:
        #             print ("here 3")
        #             ind_to_remove.append(l)
        #             l+=2
        #             r-=1
        #             continue
        #         else:
        #             print ("here 4")
        #             ind_to_remove.append(l)
        #             ind_to_remove.append(r)
        #             l+=1
        #             r-=1
        #             continue
        # for x in reversed(sorted(ind_to_remove)):
        #     s=s[:x]+s[x+1:]
        # print(ind_to_remove, s)
        # return len(s)
        
        # def recurs(l, r):
        #     if l>r:
        #         return 0
        #     if l==r:
        #         return 1
        #     if s[l]==s[r]:
        #         return 2+recurs(l+1, r-1)
        #     else:
        #         return max(recurs(l,r-1), recurs(l+1, r))
        # out = recurs(0, len(s)-1)
        # return out
        
        
        
#         n = len(s)
#         def dp(l, r):
#             if l > r: return 0  # Return 0 since it's empty string
#             if l == r: return 1  # Return 1 since it has 1 character
#             if s[l] == s[r]:
#                 return dp(l+1, r-1) + 2
#             return max(dp(l, r-1), dp(l+1, r))
        
        
        arr_2 = [[0]*len(s) for x in range(len(s))]
        
        for iters in range(len(s)):
            for ind in range(len(s)):
                if ind+iters<len(s):
                    if ind == ind+iters:
                        arr_2[ind][ind+iters]=1
                    else:
                        if s[ind] == s[ind+iters]:
                            arr_2[ind][ind+iters]=2+arr_2[ind+1][ind+iters-1]
                        else:
                            arr_2[ind][ind+iters]=max(arr_2[ind+1][ind+iters], arr_2[ind][ind+iters-1])
        # print(arr_2)
        return  (arr_2[0][len(s)-1])
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    