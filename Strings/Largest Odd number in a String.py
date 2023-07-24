class Solution:
    def largestOddNumber(self, num: str) -> str:
        lst = []
        oddnum = [1,3,5,7,9]
        numm = num[::-1]
        for i in range(len(numm)):
            if int(numm[i]) in oddnum:
                lst.append(num[0:len(num)-i])
                break
       
        return "".join(lst)
