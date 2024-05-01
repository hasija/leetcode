class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for ind, i in enumerate(word):
            if i == ch:
                return ''.join(list(reversed(word[:ind+1])))+word[ind+1:]
        return word