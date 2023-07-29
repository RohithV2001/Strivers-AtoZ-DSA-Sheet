class Solution:
    def myAtoi(self, s: str) -> int:
        def atoi(s,i,sign,res):
            if i>=len(s) or (s[i] not in '0123456789') :
                if res>=2**31 or res<=-2**31:
                    if sign==1:
                        return (2**31)-1
                    else:
                        return -2**31
                return res*sign
            if s[i] in '0123456789':
                t=s[i]
            if res>=2**31 or res<=-2**31:
                if sign==1:
                    return (2**31)-1
                else:
                    return -2**31
            return atoi(s,i+1,sign,res*10+int(t))

        i=0
        s=s.strip()
        sign=1
        if len(s)==0:
            return 0
        if s[i]=='-':
            sign=(-sign)
            i+=1
        elif s[i]=='+':
            i+=1
        return atoi(s,i,sign,0)
