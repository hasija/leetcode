class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        len_ = len(searchWord)
        for idx, w in enumerate(sentence):
            if searchWord == w[0:len_]:
                return idx+1
        return -1