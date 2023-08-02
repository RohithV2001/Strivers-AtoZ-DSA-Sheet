class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."] * n for _ in range(n)]
        ans=[]
        def issafe(row,col,board):
            dr=row
            dc=col
            while row>=0 and col>=0:
                if board[row][col]=="Q":
                    return False
                row-=1
                col-=1
            row=dr
            col=dc
            while col>=0:
                if board[row][col]=="Q":
                    return False
                col-=1
            row=dr
            col=dc
            while row<len(board) and col>=0:
                if board[row][col]=="Q":
                    return False
                row+=1
                col-=1
            return True
        def queen(col,board,ans):
            if col==n:
                ans.append(["".join(row) for row in board])
                return
            for row in range(n):
                if issafe(row,col,board):
                    board[row][col]="Q"
                    queen(col+1,board,ans)
                    board[row][col]="."
        queen(0,board,ans)
        return ans
        
