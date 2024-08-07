class Solution:
    def numberToWords(self, num: int) -> str:
        below_ten = ["","One", "Two", "Three", "Four", "Five", "Six",
                    "Seven", "Eight", "Nine"]
        below_teen = ["Ten","Eleven","Twelve", "Thirteen", "Fourteen","Fifteen",
                     "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        below_hundred = ["","Ten","Twenty", "Thirty", "Forty","Fifty","Sixty", "Seventy", "Eighty", "Ninety"]
        
        
        def helper_func(curr):
            word = []
            if curr>=100:
                curr_base = curr//100
                # print ("Basew", curr_base)
                if curr_base:
                    word.append(below_ten[curr_base])
                word.append("Hundred")
                curr %= 100
           

            if curr>19:
                # print ("Curr in above 19", curr, curr//10)
                if curr//10:
                    word.append(below_hundred[curr//10])
                curr = curr%10
                if curr:
                    word.append(below_ten[curr])
            elif curr>=10:
                word.append(below_teen[curr%10])
            else:
                if curr:
                    word.append(below_ten[curr])
            return word
        n = num
        word = []
        if n>=1000000000:
            curr = n//1000000000
            word.extend(helper_func(curr))
            word.append('Billion')
            n %= 1000000000
        if n>=1000000:
            curr = n//1000000
            word.extend(helper_func(curr))
            word.append('Million')
            n %= 1000000
        if n>=1000:
            curr = n//1000
            word.extend(helper_func(curr))
            word.append('Thousand')
            n %= 1000
        
        if len(word)==0 and n==0:
            return "Zero"
        else:
            word.extend(helper_func(n))
        
            
        return ' '.join(word).strip()

            