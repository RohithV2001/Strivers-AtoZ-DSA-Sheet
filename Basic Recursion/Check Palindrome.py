def isPalindrome(string: str) -> bool:
    st=0
    e=len(string)-1
    return palindrome(string,st,e)

def palindrome(string,st,e):
    if st==e:
        return True
    
    if string[st]!=string[e]:
        return False
    if st<=e:
        return palindrome(string,st+1,e-1)
    return True
