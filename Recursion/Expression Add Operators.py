class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(i, path, resultSoFar, prevNum):
            if i == len(num):
                if resultSoFar == target:
                    ans.append(path)
                return

            for j in range(i, len(num)):
                if j > i and num[i] == '0': break 
                s = int(num[i:j + 1])
                if i == 0:
                    backtrack(j + 1, path + str(s), resultSoFar + s, s)  
                else:
                    backtrack(j + 1, path + "+" + str(s), resultSoFar + s, s)
                    backtrack(j + 1, path + "-" + str(s), resultSoFar - s, -s)
                    backtrack(j + 1, path + "*" + str(s), resultSoFar - prevNum + prevNum * s, prevNum * s)  

        ans = []
        backtrack(0, "", 0, 0)
        return ans
