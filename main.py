from tools import board, tools

# Initial setup
# Get the filename from the user
filename = input("Where is your board located? ")

# Try to open the file
try:
   file = open(filename, "r")
except:
   print("Unable to open file '%s'" %filename)
   quit()

# Read the file and populate the board
b = board.Board
b.fillBoard(b, file)

# Display instructions
tools.displayOptions()

# Print the board
tools.printBoard(b)

# Go into the game system
while True:
   # Get the user's command
   userInput = input("\n> ")

   # Change it to upper
   userInput = userInput.upper()

   # Interpret the command
   if userInput == '?':
      tools.displayOptions()

   elif userInput == 'D':
      tools.printBoard(b)

   elif userInput == 'S':
      userCoor = input("What are the coordinates of the square: ")
      c = tools.handleInput(userCoor)
      print("The possible values for '" + tools.numToLetter(c.y) + str(c.x + 1) + "' are: ", end='')
      print(tools.makeList(tools.checkPossibilities(b.board, c)))

   elif userInput == 'E':
      userCoor = input("What are the coordinates of the square: ")
      c = tools.handleInput(userCoor)
      value = input("What is the value at '" + tools.numToLetter(c.y) + str(c.x + 1) + "': ")
      if not tools.isPossible(b.board, c, value):
         print("ERROR: the value '" + value + "' in square '" + tools.numToLetter(c.y) + str(c.x + 1) + "' is invalid.")
      else:
         b.board[c.x][c.y] = value

   elif userInput == 'Q':
      tools.saveGame(filename, b.board)
      break

   else:
      print("Invalid command")

