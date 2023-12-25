class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dp(word):
            # print(word)
            if word in memo:
                return memo[word]
            total = 0
            if len(word)==1:
                if word[0]=='0':
                    return 0
                return 1
            for i in range(1,3):
                curr = int(word[:i])
                # print("new word formed", curr, 'rest', word[i:])
                if word[:i][0]=='0':
                    return 0
                if curr>0 and curr<=26:
                    if len(word[i:])>0:
                        total+=dp(word[i:])
                    else:
                        total+=1
                    # print ("Output of word", curr, "with i ", i)
            memo[word]=total
            return total
        return dp(s)
        