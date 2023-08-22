class Solution:
    def minPartition(self, N):
        l=[]
        arr=[1,2,5,10,20,50,100,200,500,2000]
        for i in range(len(arr)-1,-1,-1):
            while N>=arr[i]:
                N-=arr[i]
                l.append(arr[i])
        return l
