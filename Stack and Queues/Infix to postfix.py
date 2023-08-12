from collections import deque
def infixToPostfix(exp: str) -> str:
    output=""
    opr={'+':1,'-':1,'*':2,'/':2,'^':3,'(':0}
    prec=deque()
    for i in exp:
        if i=='(':
            prec.append(i)
        elif i==')':
            while prec[-1]!='(':
                output+=prec.pop() 
            prec.pop()   
        elif i in opr:
            while prec and opr[i]<=opr[prec[-1]]:
                output+=prec.pop()
            prec.append(i)
        else:
            output+=i
    while prec:
        output+=prec.pop()
    return output
