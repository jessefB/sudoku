from tools import coordinate

class Board:
   board = [[None for i in range(9)] for n in range(9)]
   readable = [[0 for i in range(9)] for n in range(9)]

   def __init__(self):
       pass

   def readOnly(self, c: coordinate.Coordinate):
      return self.readable[c.x][c.y]
   
   def readOnly(self, x, y):
      return self.readable[x][y]

   def fillBoard(self, file):
      row = 0
      col = 0
      for char in file.read():
         if char == '\n':
            col = 0
            row += 1
         else:
            if char.isdigit():
               self.board[row][col] = char
               self.readable[row][col] = 1
            else:
               self.board[row][col] = " "
            col += 1
