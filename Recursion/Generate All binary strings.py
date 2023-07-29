def binary(k,out,ld,l):
    if k==0:
        l.append(out)
        return
    binary(k-1,out+'0',0,l)
    if ld==0:
        binary(k-1,out+'1',1,l)
def generateString(k):
    out=''
    ld=0
    l=[]
    binary(k,out,ld,l)
    return l
