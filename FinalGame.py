#Deeya Bachani
#K_UP=up arrow
#K_DOWN=down arrow
#K_LEFT=left arrow
#K_RIGHT= right arrow
import pygame, time, sys,os
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
green=[50,25,255]
#create an object to open window
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



clock=pygame.time.Clock()



check =True
while check:
    screen.fill(purple)
    speed=15
    clock.tick(speed)
    keyBoardKey=pygame.key.get_pressed() #checking what key is pressed
    if keyBoardKey[pygame.K_LEFT]: #moving left on x (-)
        howieImg=howieImg_left
        x-=speed
        a-=speed
    if keyBoardKey[pygame.K_RIGHT]:
        howieImg=howieImg_right
        x +=speed
        a +=speed
    if keyBoardKey[pygame.K_UP]: #moving left on x (-)
        howieImg=howieImg_front
        y-=speed
    if keyBoardKey[pygame.K_DOWN]:
        howieImg=howieImg_back
        y +=speed

    screen.blit(bg,(a,b))#create image on top of other one
    screen.blit(howieImg,(x,y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check = False
pygame.quit()







     