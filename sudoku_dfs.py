import time

class State(object):    
    def __init__(self,board):
        self.board = board
        
    def is_goal(self):
        row, col = self.findBlank()
        return row == -1 and col == -1

    def findBlank(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1 # if no blank, game is finished
    
    def checkRow(self, row, num):
        return num not in self.board[row]
    
    def checkCol(self, col, num):
        for r in range(9):
            if self.board[r][col] == num:
                return False
        return True
    
    def checkBox(self, row, col, num):
        boxrow = int(row) - int(row)%3
        boxcol = int(col) - int(col)%3


        for i in range(boxrow, boxrow+3):
            for j in range(boxcol, boxcol+3):
                if num == self.board[i][j]:
                    return False
        return True

    def solve(self):
        row, col = self.findBlank()
        #no unassigned position is found, puzzle solved
        if self.is_goal():
            return True
        for num in ["1","2","3","4","5","6","7","8","9"]:
            if self.checkBox(row, col, num) and self.checkCol(col, num) and self.checkRow(row, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False 
  

def main(board):
    print(board)
    print("\n")
    start_state = State(board)
    t0 = time.time()
    solution = start_state.solve()
    t1 = time.time()
    print("Execution time: %s"%(t1-t0))
    
    if solution:
        print(start_state.board)
    else:
        print("No possible solution")


if __name__ == '__main__':
    inputboard = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    main(inputboard)