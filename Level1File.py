#Deeya Bachani
#K_UP=up arrow
#K_DOWN=down arrow
#K_LEFT=left arrow
#K_RIGHT= right arrow

#making the screen and basics of game
import pygame, time, sys,os, datetime
from pygame.locals import *
os.system('cls')
print(sys.path)
pygame.init()
pygame.time.delay(100)
WIDTH=800 
HEIGHT=800
#create the objects



white=[255, 255, 255]
purple=[200,190,0]
green=[0,255,0]
#adding images/variables
screen=pygame.display.set_mode((WIDTH,HEIGHT))

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

clock=pygame.time.Clock()

#main game function
check =True
while check:
    screen.fill(purple)
    speed=20
    clock.tick(speed)
#moving character
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
#creating rectangles to go behind images
    endrect=pygame.Rect(750, 750, 50, 50)
    pygame.draw.rect(screen, white, endrect)
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
#creating images
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

#when rects collide, the character moves, it turns green and the player gets a point
    score=0
    if pygame.Rect.colliderect(mainRect, rect1) ==True:
        score= score+1
        rect11=pygame.Rect(10,748,33,31)
        pygame.draw.rect(screen, green, rect11)
        x+=50
        y+=50
    if  pygame.Rect.colliderect(mainRect, rect2) == True:
        score= score+1
        rect12=pygame.Rect(100,275,33,31)
        pygame.draw.rect(screen, green, rect12)
        x+=50
        y+=50
    if  pygame.Rect.colliderect(mainRect, rect3) == True:
        score= score+1
        rect13=pygame.Rect(93,723,33,31)
        pygame.draw.rect(screen, green, rect13)
        x+=50
        y+=50
    if  pygame.Rect.colliderect(mainRect, rect4) == True:
        score= score+1
        rect14=pygame.Rect(28,294,33,31)
        pygame.draw.rect(screen, green, rect14)
        x+=50
        y+=50
    if  pygame.Rect.colliderect(mainRect, rect5) == True:
        score= score+1
        rect15=pygame.Rect(490,739,33,31)
        pygame.draw.rect(screen, green, rect15)
        x+=50
        y+=50
    if  pygame.Rect.colliderect(mainRect, rect6) == True:
        score= score+1
        rect16=pygame.Rect(512,563,33,31)
        pygame.draw.rect(screen, green, rect16)
        x+=50
        y+=50
    if  pygame.Rect.colliderect(mainRect, rect7) == True:
        score= score+1
        rect17=pygame.Rect(770,473,33,31)
        pygame.draw.rect(screen, green, rect17)
        x+=50
        y+=50
    if  pygame.Rect.colliderect(mainRect, rect8) == True:
        score= score+1
        rect18=pygame.Rect(339,573,33,31)
        pygame.draw.rect(screen, green, rect18)
        x+=50
        y+=50
    if  pygame.Rect.colliderect(mainRect, rect9) == True:
        score= score+1
        rect19=pygame.Rect(624,274,33,31)
        pygame.draw.rect(screen, green, rect19)
        x+=50
        y+=50
    if  pygame.Rect.colliderect(mainRect, rect10) == True:
        score= score+1
        rect20=pygame.Rect(30,50,33,31)
        pygame.draw.rect(screen, green, rect20)
        x+=50
        y+=50

    if  pygame.Rect.colliderect(mainRect, endrect) == True:

        import FinalGame #goes back to main menu when character collides with the white box
    pygame.display.update()    
#uploads the scores
    fileName="FinalGameHighScores.py"
    FILE=open(fileName, 'a')
    dt=datetime.datetime.now()
    line= str(score)
    FILE.write(line)
    FILE.write("\n")
    FILE.close()  

    
#end of game
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check = False
pygame.quit()
clock.tick(60)