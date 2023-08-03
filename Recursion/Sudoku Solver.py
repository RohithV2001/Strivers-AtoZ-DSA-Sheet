class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def sudoku(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for c in range(1,10):
                            if isvalid(board,i,j,c):
                                board[i][j]=str(c)
                                if sudoku(board):
                                    return True
                                else:
                                    board[i][j]='.'
                        return False
            return True
        def isvalid(board,row,col,c):
            for i in range(9):
                if board[i][col] == str(c):
                    return False
                if board[row][i] == str(c):
                    return False
                if board[3 * (int(row / 3)) + int(i / 3)][3 * int((col / 3)) + i % 3] == str(c):
                    return False
            return True
        sudoku(board)

        
