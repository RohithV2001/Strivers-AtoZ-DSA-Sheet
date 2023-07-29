from typing import List

def insert(stack,item):
    if len(stack)==0 or stack[-1]<item:
        stack.append(item)
    else:
        temp=stack.pop()
        insert(stack,item)
        stack.append(temp)

def sortStack(stack: List[int]) -> None:
    if len(stack)!=0:
        temp=stack.pop() 
        sortStack(stack)
        insert(stack,temp)
    return stack
