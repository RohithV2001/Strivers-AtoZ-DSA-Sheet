def findCelebrity(n, knows):
    stack=0

    for i in range(1,n):
        if knows(stack,i):
                stack=i
                
    for i in range(n):   
        if i!=stack and (not knows(i,stack) or knows(stack,i)) :
            return -1

    return stack
