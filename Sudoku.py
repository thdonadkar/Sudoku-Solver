board = [
    [0,0,0,0,4,8,0,7,2],
    [9,6,0,0,7,0,8,0,0],
    [7,0,0,6,3,1,0,0,0],
    [0,9,6,3,0,0,0,1,5],
    [5,0,8,4,9,0,0,0,0],
    [0,0,0,0,0,0,0,2,8],
    [6,0,9,8,2,3,1,5,0],
    [0,0,1,7,0,4,0,0,6],
    [3,7,0,0,0,0,2,8,0]
]

def printBrd(brd):
  for i in range(len(board)): #row 
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - - - ")
    for j in range(len(board[0])): #column
      if j % 3 == 0 and j != 0:
        print("| ", end = '')
      print(str(board[i][j]) + " ", end='')
    print('')
#printBrd fucntion end---*

def check(ans, x, y, newBrd):
# x = row number
# y = column number
  #Check condition for row
  for i in range(len(newBrd[0])):
    if newBrd[x][i] == ans and y != i:
      return False
  
  #Check condition for column
  for j in range(len(newBrd)):
    if newBrd[j][y] == ans and x != j:
      return False

  #Check condition for each sub squares
  sqrRow = x // 3
  sqrCol = y // 3
  for i in range(sqrRow * 3, (sqrRow * 3) + 3):
    for j in range(sqrCol * 3, (sqrCol * 3) + 3):
      if newBrd[i][j] == ans and i != x and j != y:
        return False
  return True
#check function end---*

def solve(brd):
  for i in range(len(brd)):
    for j in range(len(brd[0])):
      if brd[i][j] == 0:
        for s in range(1, 10): #iterate through possible numbers
          if check(s, i, j, brd):
            brd[i][j] = s
            if solve(brd): #checks the next
              return True
            else: brd[i][j] = 0 #goes back to for loop and finds another possible number
        return False #if no possible possible number found, backtrack!
  else: return True #if board has no 0 (board is done)
#solve funtion end---*


print("Before")
printBrd(board)
print("-- -- -- -- --  -- -- --")
print("After")
solve(board)
printBrd(board)