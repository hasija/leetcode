class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alpha_dict = {alpha[i]:alpha_list[i] for i in range(len(alpha))}
        
        out = set()
        
        for w in words:
            tmp=''
            for l in w:
                tmp+=alpha_dict[l]
            out.add(tmp)
        return len(out)