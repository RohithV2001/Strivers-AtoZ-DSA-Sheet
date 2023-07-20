def count(arr: [int], n: int, x: int) -> int:
    def bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

    def bisect_right(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 + 1
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        return l if nums[l] == target else -1
    
    p=(bisect_right(arr,x)-bisect_left(arr,x))
    if p==0:
        return 0
    else:
        return ((bisect_right(arr,x)-bisect_left(arr,x))+1)
