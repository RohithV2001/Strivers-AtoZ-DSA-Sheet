class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def searchnext(board,word,row,col,idx,m,n):
            if idx==len(word):
                return True
            if row<0 or col<0 or row==m or col==n or board[row][col]!=word[idx] or board[row][col]=='!':
                return False
            c=board[row][col]
            board[row][col]="!"
            top=searchnext(board,word,row-1,col,idx+1,m,n)
            right=searchnext(board,word,row,col+1,idx+1,m,n)
            bottom=searchnext(board,word,row+1,col,idx+1,m,n)
            left=searchnext(board,word,row,col-1,idx+1,m,n)
            board[row][col]=c
            return top or right or bottom or left
        m=len(board)
        n=len(board[0])
        idx=0
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[idx]:
                    if searchnext(board,word,i,j,idx,m,n):
                        return True
        return False
        
