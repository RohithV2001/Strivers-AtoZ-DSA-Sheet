#User function Template for python3

class Solution:
    def minTime(self, root,target):
        self.res=None
        def helper(root):
            s=[]
            s.append(root)
            while s:
                node=s.pop(0)
                if node.data==target:
                    self.res=node
                if node.left!=None:
                    self.d[node.left]=node
                    s.append(node.left)
                if node.right!=None:
                    self.d[node.right]=node
                    s.append(node.right)
            
        def burning():
            q=[]
            q.append(self.res)
            vis=dict()
            vis[self.res]=1
            mini=0
            while q:
                sz=len(q)
                flag=0
                for i in range(sz):
                    node=q.pop(0)
                    if node.left!=None and vis.get(node.left)==None:
                        flag=1
                        vis[node.left]=1
                        q.append(node.left)
                    if node.right!=None and vis.get(node.right)==None:
                        flag=1
                        vis[node.right]=1
                        q.append(node.right)
                    if self.d.get(node)!=None and vis.get(self.d[node])==None:
                        flag=1
                        vis[self.d[node]]=1
                        q.append(self.d[node])
                if flag==1:
                    mini+=1
            return mini
        self.d=dict()
        helper(root)
        return burning()
        

