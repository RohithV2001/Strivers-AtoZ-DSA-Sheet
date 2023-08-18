from typing import List




def partition(arr: List[int], l: int, r: int) -> int:
    f = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= f:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i




def kth_Smallest_Element(arr: List[int], l: int, r: int, k: int) -> int:
    if k <= r - l + 1 and k > 0:
        ind = partition(arr, l, r)
        if ind - l == k - 1:
            return arr[ind]
        if ind - l > k - 1:
            return kth_Smallest_Element(arr, l, ind - 1, k)
        return kth_Smallest_Element(arr, ind + 1, r, k - ind + l - 1)
    return float("inf")




if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 1
    print(f"Kth smallest element is {kth_Smallest_Element(arr, 0, n - 1, k)}")
