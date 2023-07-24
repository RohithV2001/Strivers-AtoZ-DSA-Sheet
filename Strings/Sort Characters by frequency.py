class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        res=''
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        dd=sorted(d.items(),key=lambda x:x[1],reverse=True)
        cd=dict(dd)
        for key,val in cd.items():
            res=res+key*val
        return res
