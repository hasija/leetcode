class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        all_words = set(dictionary)
        final = []
        for word in sentence.split():
            curr = ""
            for i in word:
                curr+=i
                if curr in all_words:
                    final.append(curr)
                    break
            else:
                final.append(word)
        
        return ' '.join(final)