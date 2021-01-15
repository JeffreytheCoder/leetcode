class Solution:
    def isValidSudoku(self, board):
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidSubbox(board)
    
    def isValidUnit(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
        
    def isValidRow(self, board):
        for row in board:
            if not self.isValidUnit(row):
                return False
        return True
    
    def isValidCol(self, board):
        # for col_idx in range(9):
        #     col = []
        #     for row in board:
        #         col.append(row[col_idx])
        #     if not self.isValidUnit(col):
        #         return False
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False
        return True
    
    def isValidSubbox(self, board):
        row_indeces = [0, 3, 6]
        col_indeces = [0, 3, 6]
        for row_idx in row_indeces:
            for col_idx in col_indeces:
                subbox = [board[subrow_idx][subcol_idx] for subrow_idx in range(row_idx, row_idx + 3) for subcol_idx in range(col_idx, col_idx + 3)]
                subbox = board[row_idx][col_idx:col_idx + 3] + board[row_idx + 1][col_idx:col_idx + 3] + board[row_idx + 2][col_idx:col_idx + 3]
                if not self.isValidUnit(subbox):
                    return False
        return True

solution = Solution()
print(solution.isValidSubbox([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
        
        