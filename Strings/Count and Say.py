class Solution:
    def countAndSay(self, n: int) -> str:
        def cas(ps:str):
            cs=""
            cd=ps[0]
            count=0
            for i in ps:
                if i!=cd:
                    cs=cs+str(count)+cd
                    cd=i
                    count=0
                count+=1
            cs+=str(count)+cd
            return cs
        a="1"
        for _ in range(n-1):
            a=cas(a)
        return a
