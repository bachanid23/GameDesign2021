#Deeya Bachani
#Final Game Menu

import os, sys, time, pygame, random, math, datetime


 

os.system('cls')

pygame.init()

 

white = [255,255,255]
BLUE=[64, 224, 208]
YELLOW=[255, 215, 0]
green=[127, 255, 0]
BLACK = [0,0,0]
ORANGE= [255,69,0]
purple=[123, 104, 238]

 

TitleFont= pygame.font.SysFont("comicsans", 80)  

WordFont=pygame.font.SysFont("helvetica", 75)

LetterFont=pygame.font.SysFont("helvetica",20)

 

WIDTH = 800 

HEIGHT = 800

 

screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill(BLUE)

pygame.display.set_caption("Final Game")

 

Wbox = 40

dist = 150


clock=pygame.time.Clock()



 

def game_Init(message):  

    screen.fill(YELLOW)

    text = WordFont.render(message, 1, BLUE)

    screen.blit(text,(50,50))

 

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

            if rect5menu.collidepoint((mx,my)):

                display_message("Goodbye!")

                pygame.quit()

                sys.exit()

        pygame.display.update() 

 

def display_message(message):

    pygame.time.delay(500)

    screen.fill(ORANGE)

    text = WordFont.render(message, 1, purple)

    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))

    pygame.display.update()

    pygame.time.delay(2000)

 

def level1():

        import FinalGamereal
            

def level2():

    display_message("You are in level 2")

def level3():

    display_message("You are in level 3")

def scores():

    display_message("score function")
    display_message("Here are your scores: (in terminal)")
    import time
    fileName="FinalGameHighScores.py"
    FILE=open(fileName, 'a')
    dt=datetime.datetime.now()
    line= "had a score of " + str(score)
    FILE.write(line)
    FILE.write("\n")
    FILE.close()
    time.sleep(.5)
    FILE=open(fileName, 'r')
    print(FILE.read())
    input("Press enter when you would like to stop seeing your scores")
    FILE.close()


 

while True:

    game_Init("Final Game")

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

