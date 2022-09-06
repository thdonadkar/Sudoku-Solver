from os import system
from Sudoku import check
import pygame

#Initial the pygame
pygame.init()

#Create the GUI 
screen = pygame.display.set_mode((900, 900)) #(widht, height)

#Change Title
pygame.display.set_caption("Sudoku Solver")

#Change Icon
icon = pygame.image.load('sudoku.png')
pygame.display.set_icon(icon)

font = pygame.font.Font('freesansbold.ttf',80)

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

def solve(brd):
  for i in range(len(brd)):
    for j in range(len(brd[0])):
      if brd[i][j] == 0:
        for s in range(1, 10): #iterate through possible numbers
          if check(s, i, j, brd):
            brd[i][j] = s
            update_board()
            if solve(brd): #checks the next
              return True
            else:          #goes back to for loop and finds another possible number
              brd[i][j] = 0
              update_board() 
        return False #if no possible possible number found, backtrack!
  else: return True #if board has no 0 (board is done)
#solve funtion end---*

def board_numbers(): #display the board numbers into screen
    for row in range(9):
        for col in range(9):
            output = board[row][col]
            if (output == 0):
              n_text = font.render(str(output), True, (255,0,0))
            else:
              n_text = font.render(str(output), True, (0,0,0))
            screen.blit(n_text, pygame.Vector2((col * 99) + 30, (row * 99) + 20))

def draw_grid(): #display grid on the screen
    screen.fill((255,255,255)) #RGB colour
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(5, 5, 890, 890), 5) #drawing param. = (screen, colour, coordinates, width of line)

    off_set = 99
    #Draw the lines
    for i in range(9):
        if (i == 3) | (i == 6):
            pygame.draw.line(screen, (0,0,0), pygame.Vector2((i * off_set) + 5, 5), pygame.Vector2((i * off_set) + 5, 890), 10) #colomns 
            pygame.draw.line(screen, (0,0,0), pygame.Vector2(5, (i * off_set) + 5), pygame.Vector2(890, (i * off_set) + 5), 10) #rows
        else:
            pygame.draw.line(screen, (0,0,0), pygame.Vector2((i * off_set) + 5, 5), pygame.Vector2((i * off_set) + 5, 890), 5) #colomns 
            pygame.draw.line(screen, (0,0,0), pygame.Vector2(5, (i * off_set) + 5), pygame.Vector2(890, (i * off_set) + 5), 5) #rows

def update_board():
  draw_grid()
  board_numbers()
  pygame.time.delay(100)
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        system.exit()

#Keep the GUI running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            system.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_BACKSPACE:
            solve(board)
    draw_grid()
    board_numbers()
    pygame.display.update()