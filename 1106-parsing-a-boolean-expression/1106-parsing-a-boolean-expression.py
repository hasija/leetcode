class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        stack = []
      
      
        def get_val(op, exp):
            # print ("received exp", op, exp)
            if op=='!':
                return 'f' if exp[0]=='t' else 't'
            if op=='|':
                for val in exp:
                    if val =='t':
                        return 't'
                return 'f'
            if op=='&':
                for val in exp:
                    if val =='f':
                        return 'f'
                return 't'
            
    
        for i in exp:
            if i==')':
                tmp = []
                while stack[-1]!='(':
                    tmp.append(stack.pop())
                stack.pop() # removed open brace
                op = stack.pop() 
                stack.append(get_val(op, tmp)) # assign val back to stack
                # print ("val retn", stack[-1])
            elif i!=',':
                stack.append(i)
        return stack[-1]=='t'
      