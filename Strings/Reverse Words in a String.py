class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        temp=''
        for i in s:
            if i!=' ':
                temp+=i
            elif temp!='':
                res.append(temp)
                temp=""
        if temp!="":
            res.append(temp)
        return " ".join(res[::-1])
