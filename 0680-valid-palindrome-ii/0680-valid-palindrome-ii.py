class Solution:
    def validPalindrome(self, s: str) -> bool:
         
        def check_palin(l,r, used):
            if l==r:
                return True
            else:
                if l>r:
                    return True
                if s[l]==s[r]:
                    return check_palin(l+1,r-1, used)
                else:
                    if used:
                        return False
                    else:
                        x=check_palin(l,r-1, True)
                        y = check_palin(l+1,r, True)
                        if x or y:
                            return True
        return check_palin(0, len(s)-1, False)