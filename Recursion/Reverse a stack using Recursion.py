def insert(stack,item):
    if len(stack)==0:
        stack.append(item)
    else:
        temp=stack.pop()
        insert(stack,item)
        stack.append(temp)

def reverseStack(stack: List[int]) -> None:
    if len(stack)!=0:
        temp=stack.pop() 
        reverseStack(stack)
        insert(stack,temp)
    return stack
