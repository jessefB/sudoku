from tools.coordinate import Coordinate

# Display options
def displayOptions():
   print("Options:")
   print("   ?  Show these instructions")
   print("   D  Display the board")
   print("   E  Edit one square")
   print("   S  Show the possible values for a square")
   print("   Q  Save and Quit\n")

# Print out the board
def printBoard(board):
   # Header
   print("   A B C D E F G H I")
   for row, rVal in enumerate(board.board):
      # Print row or box lines?
      if row % 3 == 0 and row != 0:
         print("   -----+-----+-----")
      # Print row numbers
      print(str(row + 1) + " ", end='')
      for col, cVal in enumerate(rVal):
         # Spaces or box lines?
         if col % 3 == 0 and col != 0:
            print("|", end='')
         else:
            print(" ", end='')
         # Print the values
         if not board.readOnly(board, row, col) and board.board[row][col] != ' ':
            print('\033[94m' + cVal + '\033[0m', end='')
         else:
            print(cVal, end='')
      print("")

# Quit command
def saveGame(filename, board):
   # Overwrite the original file?
   overWrite = input("Overwrite original file? (Y): ") or 'Y'
   if overWrite.upper() != 'Y' and overWrite.upper() !='YES':
      overWrite = False
   else:
      overWrite = True

   # Write the original file
   if overWrite == True:
      file = open(filename, "w")
      for row in board:
         for col in row:
            if col == ' ':
               file.write('X')
            else:
               file.write(col)
         file.write('\n')
   else:
      filename = input("What file would you like to write your board to: ")
      file = open(filename, "w")
      for row in board:
         for col in row:
            if col == ' ':
               file.write('X')
            else:
               file.write(col)
         file.write('\n')

def handleInput(input):
      if input[0].isdigit():
         x = input[0]
         y = input[1].upper()
      else:
         x = input[1]
         y = input[0].upper()
      
      # Convert Y to its number
      y = {
         'A': 0,
         'B': 1,
         'C': 2,
         'D': 3,
         'E': 4,
         'F': 5,
         'G': 6,
         'H': 7,
         'I': 8
      }[y]
      
      c = Coordinate(int(x) - 1, int(y))

      return c
   
# Convert numbers back to the coordinate letters
def numToLetter(input):
   y = {
      0: 'A',
      1: 'B',
      2: 'C',
      3: 'D',
      4: 'E',
      5: 'F',
      6: 'G',
      7: 'H',
      8: 'I'
   }[input]

   return y

# Check for possible values in a given square
def checkPossibilities(board, c):
   possibleValues = []

   for i in range(1, 10):
      if isPossible(board, c, i):
         possibleValues.append(i)
   return possibleValues

# Check if possible
def isPossible(board, c, value):
   # Convert value to a string for comparisons
   value = str(value)

   # Check row
   for items in board[c.x]:
      if items == value:
         return False
   
   # Check col
   for col in range(9):
      if board[col][c.y] == value:
         return False

   # Check boxes
   # Calculate starting positions for the virtual boxes
   rowStart = int((c.x / 3)) * 3
   colStart = int((c.y / 3)) * 3

   for r in range(rowStart, rowStart + 2):
      for c in range(colStart, colStart + 2):
         if board[r][c] == value:
            return False
   
   return True

# Make a string out of a list
def makeList(values):
   output = ""

   for i, value in enumerate(values):
      if i + 1 != len(values):
         output = output + str(value) + ", "
      else:
         output = output + str(value)
   
   return output