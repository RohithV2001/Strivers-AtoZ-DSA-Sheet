def maxheapify(arr,i,n):
    l = 2 * i + 1
    r = 2 * i + 2
    largest=i
    if l<n and arr[l]>arr[i]:
        largest=i
    if r<n and arr[r]>arr[largest]:
        largest=i
    while largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        maxheapify(arr,largest,n)
def MinToMaxHeap(n, arr):
    for i in range(int((n-2)/2),-1,-1):
        maxheapify(arr,i,n)
    return arr

n=int(input())
arr=list(map(int,input().split()))
final=MinToMaxHeap(n,arr)
print(final)
