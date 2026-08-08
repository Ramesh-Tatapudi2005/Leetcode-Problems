class Solution:
    def checksudoku(self, row, col, board, val):
        for i in range(9):
            if i != row and board[i][col]== val:
                return False
            if i != col and board[row][i] == val:
                return False
            val1 = 3 * (row // 3) +  (i // 3)
            val2 = 3 *(col// 3 ) + (i  % 3)
            if val1 != row and val2 != col and board[val1][val2] == val:
                return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boo = True
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    boo = self.checksudoku(row,col,board,board[row][col])
                    if boo==False:
                        return False
        return True