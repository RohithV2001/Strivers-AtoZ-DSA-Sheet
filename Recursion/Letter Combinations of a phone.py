class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
                        "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz"
                        }
        res=[]
        if len(digits)==0:
            return res
        
        def dfs(digits,idx,keyboard,ans,res):
            if idx>=len(digits):
                res.append(ans)
                return
            st1=keyboard[digits[idx]]
            for i in st1:
                dfs(digits,idx+1,keyboard,ans+i,res)
        
        dfs(digits,0,keyboard,'',res)
        return res
