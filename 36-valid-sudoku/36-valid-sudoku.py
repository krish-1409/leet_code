class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            dic = [0 for _ in range(10)]
            for j in range(9):
                if board[i][j]=='.':
                    continue
                else:
                    if dic[int(board[i][j])]==1:
                        return False
                    else:
                        dic[int(board[i][j])]+=1
        
        for i in range(9):
            dic = [0 for _ in range(10)]
            for j in range(9):
                if board[j][i]=='.':
                    continue
                else:
                    if dic[int(board[j][i])]==1:
                        return False
                    else:
                        dic[int(board[j][i])]+=1
        
        
        dic = [[0 for _ in range(10)] for _  in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if dic[i//3+(3*(j//3))][int(board[i][j])] == 1:
                        return False
                    else:
                        dic[i//3+(3*(j//3))][int(board[i][j])] = 1
        return True
                
            