class Solution:
    def countOfAtoms(self, formula: str) -> str:
        cnt = defaultdict(int)
        n = len(formula)
        digit = ''
        lower = ''
        stack = [1]
        
        for i in range(n-1, -1, -1):
            curr = formula[i]
            if curr.isdigit():
                digit = curr+digit
                continue
            elif curr.islower():
                lower = curr+lower
                continue
            elif curr == ')':
                stack.append(stack[-1]*int(digit or 1))
                digit = ''
                lower = ''
            elif curr == '(':
                stack.pop()
                continue
            else:
                final_score = int(digit or 1)*stack[-1]
                final = curr+lower
                cnt[final] += final_score
                digit = ''
                lower = ''
        keys = sorted(list(cnt.keys()))
        ans = ""
        for key in keys:
            ans+=key+str(cnt[key] if cnt[key]>1 else "")
        return ans
                
                
                