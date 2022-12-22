import pygame
import random
import time

pygame.init()

pygame.font.init()

#Creating fonts 
myfont = pygame.font.SysFont('Courier New', 20)
myfont_win=pygame.font.SysFont('Times New Roman', 80)

#Defining RGB values for colours
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)
GOLD=( 230, 215, 0)

#a screen for display
screen = pygame.display.set_mode((800,600)) 
pygame.display.set_caption('2048') 
clock = pygame.time.Clock() 

board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

points = 0
score = 0
continue_after_win = 0
draw_state = 0

try:
    with open('highscore.txt' , 'r') as file:
        highest_score = int(file.readline())

except:
    highest_score=0

def initial():
    count = 0
    while count < 2:
        row = random.randrange(0, 4)
        col = random.randrange(0, 4)
        if board[row][col] == 0:
            n = random.randrange(2, 5, 2)
            board[row][col] = n
            count = count + 1
            textsurface = myfont.render(str(n), False, GOLD)
            screen.blit(textsurface, (250+100*col, 150 + row*100))
    pass

def gen():
    flag = False
    while flag == False:
        row = random.randrange(0, 4)
        col = random.randrange(0, 4)
        if board[row][col] == 0:
            n = random.randrange(2, 5, 2)
            board[row][col] = n
            flag = True
            textsurface = myfont.render(str(n), False, GOLD)
            screen.blit(textsurface, (250+100*col, 150 + row*100))

def move_up():
    global score
    for i in range(0, 4):
        count = 0
        for j in range(1, 4):
            if board[j][i] != 0:
                for k in range(0, j):
                    if board[j-1-k][i] == 0:
                        board[j-1-k][i] = board[j-k][i]
                        board[j-k][i] = 0
                    elif board[j-1-k][i] == board[j-k][i] :
                        if count == 0:
                            board[j-1-k][i] = board[j-k][i] * 2
                            score = score + board[j-k][i] * 2
                            board[j-k][i] = 0
                            count = 1
                        break
                    elif board[j-1-k][i] != board[j-k][i]:
                        break
    pass

def move_down():
    global score
    for i in range(0, 4):
        count = 0
        for j in range(2, -1, -1):
            if board[j][i] != 0:
                for k in range(j, 3):
                    if board[k+1][i] == 0:
                        board[k+1][i] = board[k][i]
                        board[k][i] = 0
                    elif board[k+1][i] == board[k][i]:
                        if count == 0:
                            board[k+1][i] = board[k][i] * 2
                            score = score + board[k][i] * 2
                            board[k][i] = 0
                            count = count + 1
                        break
                    elif board[k+1][i] != board[k][i]:
                        break
    pass

def move_left():
    global score
    for i in range(0, 4):
        count = 0
        for j in range(1, 4):
            if board[i][j] != 0:
                for k in range(0, j):
                    if board[i][j-1-k] == 0 :
                        board[i][j-1-k] = board[i][j-k]
                        board[i][j-k] = 0
                    elif board[i][j-1-k] == board[i][j-k]:
                        if count == 0:
                            board[i][j-1-k] = board[i][j-k] * 2
                            score = score + board[i][j-k] * 2
                            board[i][j-k] = 0
                            count = count + 1
                        break
                    elif board[i][j-1-k] != board[i][j-k]:
                        break
    pass

def move_right():
    global score
    for i in range(0, 4):
        count = 0
        for j in range(2, -1, -1):
            if board[i][j] != 0:
                for k in range(j, 3):
                    if board[i][k + 1] == 0:
                        board[i][k + 1] = board[i][k]
                        board[i][k] = 0
                    elif board[i][k+1] == board[i][k]:
                        if count == 0:
                            board[i][k+1] = board[i][k] * 2
                            score = score + board[i][k] * 2
                            board[i][k] = 0
                            count = 1
                        break
                    elif board[i][k+1] != board[i][k]:
                        break
    pass

def gen_board():
    screen.fill(BLACK)
    for i in range (0,5):
        pygame.draw.line(screen, WHITE, (200,100*(i+1) ), (600, 100*(i+1)))
        pygame.draw.line(screen, WHITE, (200+100*i,100 ), (200+100*i,500 ))
    textsurface = myfont.render('Score', False, GREEN)
    screen.blit(textsurface,(660,50))            

    textsurface = myfont.render('Highest Score', False, RED)
    screen.blit(textsurface,(630,120)) 
    for row in range(0, 4):
        for col in range(0, 4):
            if board[row][col] != 0:
                textsurface = myfont.render(str(board[row][col]), False, GOLD)
                screen.blit(textsurface, (250+100*col, 150 + row*100)) 
    pass

def score_update():
    global score, highest_score
    textsurface = myfont.render(str(score), False, WHITE)
    screen.blit(textsurface, (660, 70))
    if score > highest_score:
        highest_score = score
    textsurface = myfont.render(str(highest_score), False, WHITE)
    screen.blit(textsurface, (660, 140))

def highScoreUpdate():
    if highest_score < score:
        f = open("highscore.txt", "w")
        f.write(str(highest_score))
        f.close()
            
def GameOver():
    adj_hor = adj_vert = all_cells = 0
    for i in range(0, 4):
        for j in range(0, 3):
            if board[i][j] == board[i][j+1]:
                adj_hor = 1
                break
        if adj_hor > 0:
            break
    for i in range(0, 4):
        for j in range(0, 3):
            if board[j][i] == board[j+1][i]:
                adj_vert = 1
                break
        if adj_vert > 0:
            break
    for i in range(0, 4):
        if board[i].count(0) > 0:
            all_cells = 1
            break
    if all_cells == adj_hor == adj_vert == 0:
        textsurface = myfont.render("Game Over !!!", False, RED)
        screen.blit(textsurface,(300,50))
    return 1

###### MAIN   ############


for i in range (0,5):

    pygame.draw.line(screen, WHITE, (200,100*(i+1) ), (600, 100*(i+1)))
    pygame.draw.line(screen, WHITE, (200+100*i,100 ), (200+100*i,500 ))

textsurface = myfont.render('Score', False, GREEN)
screen.blit(textsurface,(660,50))            

textsurface = myfont.render('Highest Score', False, RED)
screen.blit(textsurface,(630,120)) 
# clock.tick(1000)
initial()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(score)
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()
            elif event.key == pygame.K_UP:
                move_up()
            elif event.key == pygame.K_DOWN:
                move_down()
        # time.sleep(4)
        # pygame.display.flip()
        if event.type == pygame.KEYUP:
            gen()
            gen_board()
            highScoreUpdate()
            score_update()
            GameOver() 
    pygame.display.update()