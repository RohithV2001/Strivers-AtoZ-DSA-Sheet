def sortList(head):
    c=[0,0,0]
    temp=head
    while temp:
        c[temp.data]+=1
        temp=temp.next
    temp=head
    i=0
    while temp:
        if c[i]==0:
            i+=1
        else:
            temp.data=i
            c[i]-=1
            temp=temp.next
    return head
