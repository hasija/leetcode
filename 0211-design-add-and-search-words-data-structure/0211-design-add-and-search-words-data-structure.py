class Tree:
    def __init__(self, val=None, word=False):
        self.next = {}
        self.word= word
        self.val=val

class WordDictionary:

    def __init__(self):
        self.start = Tree()
        self.found = False
    def addWord(self, word: str) -> None:
        s  = self.start
        for val in word:
            if val in s.next:
                pass
            else:
                s.next[val]=Tree(val)
            s = s.next[val]
        s.word=True
    
    def check_word(self, word, curr, s):
        val = word[curr]
        if self.found:
            return
        # Final Situtation to handled seprately
        if curr == len(word)-1:
            if val !='.':
                if val in s.next and s.next[val].word:
                    self.found=True
                    return
                else:
                    return False
            elif val=='.':
                for new_val in s.next:
                    if s.next[new_val].word:
                        self.found=True
                return False
            else:
                return False
            
        
    
    
    
        if val!='.':
            if val in s.next:
                s = s.next[val]
                self.check_word(word, curr+1, s)
        elif val=='.':
            for new_val in s.next:
                self.check_word(word, curr+1, s.next[new_val])
        else:
            return
        

            
            
    
    def search(self, word: str) -> bool:
        s  =self.start
        self.check_word(word, 0, self.start)
        out = True if self.found else False
        self.found=False
        return out


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)