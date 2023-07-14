class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for i in nums:
            xor^=i
        return xor

'''O(n) Time and O(1) space'''
