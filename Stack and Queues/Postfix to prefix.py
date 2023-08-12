def postfixToPrefix(s: str) -> str:
    stack=[]
    n=len(s)-1
    i=0
    while i<=n:
        if not operator(s[i]):
            stack.append(s[i])
            i+=1
        else:
            a=stack.pop()
            st=s[i]+stack.pop()+a
            stack.append(st)
            i+=1
    return stack.pop()
def operator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
