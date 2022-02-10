class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        letter_dict={}
        for x in chars:
            if x in letter_dict:
                letter_dict[x]+=1
            else:
                letter_dict[x]=1
        total = 0
        for x in words:
            copy_dict = letter_dict.copy()
            flag=True
            for y in x:
                if y in copy_dict and copy_dict[y]>0:
                    copy_dict[y]-=1
                else:
                    flag=False
                    break
            if flag:
                total+=len(x)
                
        return total