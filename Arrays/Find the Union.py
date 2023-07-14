def sortedArray(a: [int], b: [int]) -> [int]:
    i=0
    j=0
    final=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            if len(final)==0 or final[-1]!=a[i]:
                final.append(a[i])
            i+=1
        else:
            if len(final)==0 or final[-1]!=b[j]:
                final.append(b[j]) 
            j+=1
    while i<len(a):
        if final[-1]!=a[i]:
            final.append(a[i])
        i+=1
    while j<len(b):
        if final[-1]!=b[j]:
            final.append(b[j])
        j+=1
