class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        total_word = len(words[0])
        t_len = len(target)
        dp = [[0]*26 for i in range(total_word)]
        for val in words:
            for ind, char in enumerate(val):
                char_ind = ord(char)-97
                # print (char_ind)
                dp[ind][char_ind]+=1
       
        memo = {}
        @lru_cache
        def dfs(word, ind):
            if (word,ind) in memo:
                return memo[(word,ind)]
            # print ("initiate", word, ind)
            if word=='':
                return 1
            if ind>=total_word:
                return 0
            char = word[0]
            char_ind = ord(char)-97
            total = 0
            word_left = len(word[1:])
            for i in range(ind, total_word-word_left):
                if dp[i][char_ind]:
                    res = dfs(word[1:], i+1)
                    total+= dp[i][char_ind]*res
                    # print ("res receive", word, ind, 'res',res, dp[i][char_ind], i)
            # print ("return receiv", total,'of input', word, ind)
            memo[(word,ind)]=total
            return total
        
        return dfs(target, 0)%(10**9 + 7)