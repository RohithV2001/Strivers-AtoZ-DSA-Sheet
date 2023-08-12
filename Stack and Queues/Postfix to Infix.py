def postToInfix(postfix: str) -> str:
    s=[]
    for i in postfix:
        if not operator(i):
            s.insert(0,i)
        else:
            op1=s.pop(0)
            op2=s.pop(0)
            s.insert(0,'('+op2+i+op1+')')
    return s.pop()


def operator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
