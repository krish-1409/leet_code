class Solution:
    def setZeroes(self, board: List[List[int]]) -> None:
        isCol = False
        n = len(board)
        m = len(board[0])
        for i in range(n):
            if board[i][0]==0:
                isCol = True
            for j in range(1,m):
                if board[i][j]==0:
                    board[i][0] = 0
                    board[0][j] = 0
        print(board)
        for i in range(1,n):
            if board[i][0]==0:
                for j in range(m):
                    board[i][j] = 0
        for j in range(1,m):
            if board[0][j]==0:
                for i in range(n):
                    board[i][j]=0
        
        if board[0][0]==0:
            for j in range(m):
                board[0][j]=0
        if isCol:
            for i in range(n):
                board[i][0]=0
        
        """
        1 2  3   0
        5 0  7   8
        0 10 11 12
        0 14 15 0 
        
        
        """