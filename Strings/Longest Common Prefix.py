'''Using String Slicing'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        first = strs[0]
        for y in range(0, len(first)):
            result += first[y]
            for x in strs[1:]:
                if result not in x[:y+1]:
                    return result[:-1]
            
        return result

'''Using Python zip function '''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=""
        for i in zip(*strs):
            if len(set(i))==1:
                p=p+i[0]
            else:
                break
        return p
