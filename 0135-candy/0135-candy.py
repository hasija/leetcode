class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1]*n
    
    
        def logic(i,cond):
            if cond=='left':
                prev = ratings[i-1]
                p_c = candy[i-1]
            else:
                prev = ratings[i+1]
                p_c = candy[i+1]
            curr = ratings[i]
            c = candy[i]
            if prev<curr:
                if p_c>=c:
                    candy[i]=p_c+1

            else:
                pass
        
        for i in range(1,n):
            # print ('check',i,ratings[i])
            # print (candy)
            logic(i,'left')
            # print("after",candy)
            
        
        for j in range(n-2, -1, -1):
            logic(j,'right')
        # print (candy)
        return sum(candy)