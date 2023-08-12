def countGreater(N: int, Q: int, arr: List[int], query: List[int]) -> List[int]:
    l=[]
    for i in query:
        c=0
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                c+=1
        l.append(c)
    return l
