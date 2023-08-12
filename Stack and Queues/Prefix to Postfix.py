from typing import List

def preToPost(s: str) -> str:
    stack=[]
    i=len(s)-1
    while i>=0:
        if not operator(s[i]):
            stack.append(s[i])
            i-=1
        else:
            st=stack.pop()+stack.pop()+s[i]
            stack.append(st)
            i-=1
    return stack.pop()
def operator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
