#Deeya Bachani
#Final Game

import os, sys, time, pygame, random, math, datetime


 

os.system('cls')

pygame.init()

 
#making colors
white = [255,255,255]
BLUE=[64, 224, 208]
YELLOW=[255, 215, 0]
green=[127, 255, 0]
BLACK = [0,0,0]
ORANGE= [255,69,0]
purple=[123, 104, 238]

 
#making text
TitleFont= pygame.font.SysFont("comicsans", 80)  

WordFont=pygame.font.SysFont("helvetica", 75)

LetterFont=pygame.font.SysFont("helvetica",20)

 
#making screen/basics of the game
WIDTH = 800 

HEIGHT = 800

 

screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill(BLUE)

pygame.display.set_caption("Final Game")

 

Wbox = 40

dist = 150


clock=pygame.time.Clock()



 
#main game menu code
def game_Init(message):  

    screen.fill(YELLOW)

    text = WordFont.render(message, 1, BLUE)

    screen.blit(text,(50,50))

 
#making rectangles for menu screen
    rect1menu=pygame.Rect(50, 150, Wbox*2,Wbox*2)

    pygame.draw.rect(screen, green, rect1menu, width=1)

    text = LetterFont.render("1", 1, purple)

    screen.blit(text, (60 , 150))

 

    rect2menu=pygame.Rect(50, 250, Wbox*2,Wbox*2)

    pygame.draw.rect(screen, green, rect2menu, width=1)

    text = LetterFont.render("2", 1, purple)

    screen.blit(text, (60 , 250))

    

    rect3menu=pygame.Rect(50, 350, Wbox*2,Wbox*2)

    pygame.draw.rect(screen, green, rect3menu, width=1)

    text = LetterFont.render("3", 1, purple)

    screen.blit(text, (60 , 350))



    rect4menu=pygame.Rect(50, 450, Wbox*2,Wbox*2)

    pygame.draw.rect(screen, green, rect4menu, width=1)

    text = LetterFont.render("Scores", 1, purple)

    screen.blit(text, (60 , 450))


    rect5menu=pygame.Rect(50, 550, Wbox*2,Wbox*2)

    pygame.draw.rect(screen, green, rect5menu, width=1)

    text = LetterFont.render("Exit", 1, purple)

    screen.blit(text, (60 , 550))


    rect6menu=pygame.Rect(50, 650, Wbox*2,Wbox*2)

    pygame.draw.rect(screen, green, rect6menu, width=1)

    text = LetterFont.render("Instructions", 1, purple)

    screen.blit(text, (60 , 650))

    

    
#instructions for what to do when each rectangle is clicked
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit() 

        if event.type == pygame.MOUSEBUTTONDOWN:

            mx,my= pygame.mouse.get_pos()

            if rect1menu.collidepoint((mx,my)):

                #call main function

                level1()
            

            if rect2menu.collidepoint((mx,my)):

                level2()

            if rect3menu.collidepoint((mx,my)):

                level3()

            if rect4menu.collidepoint((mx,my)):
                
                scores()

            if rect6menu.collidepoint((mx, my)):

                instructions()

            if rect5menu.collidepoint((mx,my)):

                display_message("Goodbye!")

                pygame.quit()

                sys.exit()

        pygame.display.update() 

 
#function for any text
def display_message(message):

    pygame.time.delay(500)

    screen.fill(ORANGE)

    text = WordFont.render(message, 1, purple)

    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))

    pygame.display.update()

    pygame.time.delay(2000)

 
#if a level is clicked, that level file is imported
def level1():

    display_message("You are in level 1")
    import Level1File
    


def level2():

    display_message("You are in level 2")
    import Level2File

def level3():

    display_message("You are in level 3")
    import Level3File
#scores are found in the FinalGameHighScores.py file. Then transfered to Written scores to be concise.
def scores():

    display_message("score function")
    display_message("Scores are in the terminal")
    import time
    print("TOP SCORES:")
    print("1. 192")
    print("2. 84")
    print("3. 79")
    print("your score=")
    given_file= open('FinalGameHighScores.py', 'r')

    lines= given_file.readlines()
    sum=0

    for line in lines:
        for c in line:
            if c.isdigit() == True:
                sum= sum+ int(c)
    print(sum)
    given_file.close()
    
    otherfile= open ("WrittenScores.py", 'w')
    number= str(sum)
    otherfile.write("score=" +number)
    otherfile.write("\n")
    otherfile.close
    open("FinalGameHighScores.py", 'w').close()
    fileName="WrittenScores.py"
    FILE=open(fileName, 'r')
    print(FILE.read())
    FILE.close()
    game_Init("Final Game Menu")

#The instructions are written with this function
def instructions():
    screen.fill(purple)
    text = TitleFont.render("Instructions:", 1, BLACK)
    screen.blit(text, (100,100))
    step1 = LetterFont.render("1.Use the arrow keys to move", 1, BLACK)
    screen.blit(step1, (100,200))
    step2 = LetterFont.render("2.Everytime you hit a dragon, you get a point", 1, BLACK)
    screen.blit(step2, (100, 300))
    step3 = LetterFont.render("3.Hit the white box in the bottom right corner", 1, BLACK)
    screen.blit(step3, (100, 400))
    step4 = LetterFont.render("with your character to get back to the menu", 1, BLACK)
    screen.blit(step4, (100, 450))
    step5 = LetterFont.render("ENJOY THE GAME!", 1, BLACK)
    screen.blit(step5, (100,550))
    pygame.time.delay(2000)
    pygame.display.update

 
#playing the game
while True:

    game_Init("Final Game")

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

