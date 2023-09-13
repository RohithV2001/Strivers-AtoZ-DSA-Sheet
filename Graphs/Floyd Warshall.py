#User function template for Python

class Solution:
    def shortest_distance(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==-1:
                    matrix[i][j]=float('inf')
                if i==j:
                    matrix[i][j]=0
        for k in range(len(matrix)):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=-1
        
