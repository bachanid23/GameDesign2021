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

    check=True
    while check==True:
        howieImg_front=pygame.image.load("Images/howieImg_front.png").convert_alpha() #MAKE MUCH SMALLER
        howieImg_back=pygame.image.load("Images/howieImg_back.png").convert_alpha()
        howieImg_right=pygame.image.load("Images/howieImg_right.png").convert_alpha()
        howieImg_left=pygame.image.load("Images/howieImg_left.png").convert_alpha()

        howieImg= howieImg_front

        x=20
        y=20
        a=0
        b=0
        bg=pygame.image.load(os.path.join("Images/gameBackground.png")). convert() #MAKE MUCH BIGGER
        bg = pygame.transform.scale(bg, (1280, 720))

        bad=pygame.image.load("Images/badcharacter (1).jpg")

        screen.fill(purple)
        speed=15
        clock.tick(speed)

        keyBoardKey=pygame.key.get_pressed() #checking what key is pressed
        if keyBoardKey[pygame.K_LEFT]: #moving left on x (-)
            howieImg=howieImg_left
            x-=speed
        if keyBoardKey[pygame.K_RIGHT]:
            howieImg=howieImg_right
            x +=speed
        if keyBoardKey[pygame.K_UP]: #moving left on x (-)
            howieImg=howieImg_front
            y-=speed
        if keyBoardKey[pygame.K_DOWN]:
            howieImg=howieImg_back
            y +=speed
        

        rect1=pygame.Rect(10,748,33,31)
        pygame.draw.rect(screen, purple, rect1)
        rect2=pygame.Rect(100,275,33,31)
        pygame.draw.rect(screen, purple, rect2)
        rect3=pygame.Rect(93,723,33,31)
        pygame.draw.rect(screen, purple, rect3)
        rect4=pygame.Rect(28,294,33,31)
        pygame.draw.rect(screen, purple, rect4)
        rect5=pygame.Rect(490,739,33,31)
        pygame.draw.rect(screen, purple, rect5)
        rect6=pygame.Rect(512,563,33,31)
        pygame.draw.rect(screen, purple, rect6)
        rect7=pygame.Rect(770,473,33,31)
        pygame.draw.rect(screen, purple, rect7)
        rect8=pygame.Rect(339,573,33,31)
        pygame.draw.rect(screen, purple, rect8)
        rect9=pygame.Rect(624,274,33,31)
        pygame.draw.rect(screen, purple, rect9)
        rect10=pygame.Rect(30,50,33,31)
        pygame.draw.rect(screen, purple, rect10)
        mainRect=pygame.Rect(x,y,62,90)
        pygame.draw.rect(screen, purple, mainRect)

        screen.blit(bg,(a,b))#create image on top of other one
        screen.blit(howieImg,(x,y))
        screen.blit(bad,(30,50))
        screen.blit(bad,(10,748))
        screen.blit(bad,(100,275))
        screen.blit(bad,(93,723))
        screen.blit(bad,(28,294))
        screen.blit(bad,(490,739))
        screen.blit(bad,(512,563))
        screen.blit(bad,(770,473))
        screen.blit(bad,(339,573))
        screen.blit(bad,(624,274))


        score=0
        if pygame.Rect.colliderect(mainRect, rect1) ==True:
            score+=1
            rect11=pygame.Rect(10,748,33,31)
            pygame.draw.rect(screen, green, rect11)
            x+=50
            y+=50
        if  pygame.Rect.colliderect(mainRect, rect2) == True:
            score+=1
            rect12=pygame.Rect(100,275,33,31)
            pygame.draw.rect(screen, green, rect12)
            x+=50
            y+=50
        if  pygame.Rect.colliderect(mainRect, rect3) == True:
            score+=1
            rect13=pygame.Rect(93,723,33,31)
            pygame.draw.rect(screen, green, rect13)
            x+=50
            y+=50
        if  pygame.Rect.colliderect(mainRect, rect4) == True:
            score+=1
            rect14=pygame.Rect(28,294,33,31)
            pygame.draw.rect(screen, green, rect14)
            x+=50
            y+=50
        if  pygame.Rect.colliderect(mainRect, rect5) == True:
            score+=1
            rect15=pygame.Rect(490,739,33,31)
            pygame.draw.rect(screen, green, rect15)
            x+=50
            y+=50
        if  pygame.Rect.colliderect(mainRect, rect6) == True:
            score+=1
            rect16=pygame.Rect(512,563,33,31)
            pygame.draw.rect(screen, green, rect16)
            x+=50
            y+=50
        if  pygame.Rect.colliderect(mainRect, rect7) == True:
            score+=1
            rect17=pygame.Rect(770,473,33,31)
            pygame.draw.rect(screen, green, rect17)
            x+=50
            y+=50
        if  pygame.Rect.colliderect(mainRect, rect8) == True:
            score+=1
            rect18=pygame.Rect(339,573,33,31)
            pygame.draw.rect(screen, green, rect18)
            x+=50
            y+=50
        if  pygame.Rect.colliderect(mainRect, rect9) == True:
            score+=1
            rect19=pygame.Rect(624,274,33,31)
            pygame.draw.rect(screen, green, rect19)
            x+=50
            y+=50
        if  pygame.Rect.colliderect(mainRect, rect10) == True:
            score+=1
            rect20=pygame.Rect(30,50,33,31)
            pygame.draw.rect(screen, green, rect20)
            x+=50
            y+=50

            pygame.display.update
            

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

