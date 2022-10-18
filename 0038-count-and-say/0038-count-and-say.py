class Solution:
    def countAndSay(self, n: int) -> str:
        def get_dig_num(val):
            val = str(val)
            count=0
            prev = None
            out = []
            # print (val ,'start of get dig')
            for i in range(len(val)):
                curr = val[i]
                # print (curr, out, 'curr and out')
                if curr ==prev:
                    count+=1
                else:
                    if prev is not None:
                        out.append([prev, count]) 
                    count=1
                    prev = curr
            out.append([prev, count])
            return out
        
        def create_str(arr):
            final = []
            for val,cnt in arr:
                final.append(str(cnt))
                final.append(val)
            # print (final, 'final arr formed')
            final = int(''.join(final))
            return final
        curr = 1
        if n ==1:
            return "1"
        val = 1
        while (curr<n):
            # print (val, 'start')
            res = get_dig_num(val)
            # print (res, 'res from digital')
            val = create_str(res)
            # print (val, 'last_val')
            curr+=1
        return str(val)