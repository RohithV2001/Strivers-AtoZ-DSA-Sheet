'''Using Backtracking'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s=[]
        r=[]
        def parenthesis(on,cn):
            if cn==on==n:
                r.append("".join(s))
            if on<n:
                s.append("(")
                parenthesis(on+1,cn)
                s.pop()
            if cn<on:
                s.append(")")
                parenthesis(on,cn+1)
                s.pop()
        parenthesis(0,0)
        return r
