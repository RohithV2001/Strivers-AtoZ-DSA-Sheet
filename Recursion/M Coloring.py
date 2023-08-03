
def graphColoring(graph, k, V):
    color=[0]*V
    def isValid(node,i):
        for j in range(V):
            if graph[node][j]==1 and color[j]==i:
                return False
        return True
                
            
    def solve(node,V):
        if node==V:
            return True
        for i in range(1,k+1):
            if isValid(node,i):
                color[node]=i
                if solve(node+1,V)==True:
                    return True
                else:
                    color[node]=0
        return False
    if solve(0,V)==True:
        return True
    return False
