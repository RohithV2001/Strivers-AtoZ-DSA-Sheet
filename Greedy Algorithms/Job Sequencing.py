class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda x:x.profit,reverse=True)
        done=[0]*(101)
        ans=0
        count=0

        for i in range(n):
            dead=Jobs[i].deadline
            serial=Jobs[i].id
            cost=Jobs[i].profit
            for j in range(dead,0,-1):
                if(done[j]==0):
                    done[j]=serial
                    ans+=cost
                    count+=1
                    break
        return (count,ans)
