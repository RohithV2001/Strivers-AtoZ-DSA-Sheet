#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        c=0
        k=-1
        l=[]
        for i in range(len(start)):
            l.append([start[i],end[i]])
        l.sort(key=lambda x:x[1])
        for i in range(len(l)):
            if l[i][0]<l[i][1]:
                if l[i][0]>k:
                    c+=1
                    k=l[i][1]
        return c
                
            
