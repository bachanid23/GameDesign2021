#Deeya Bachani
#K_UP=up arrow
#K_DOWN=down arrow
#K_LEFT=left arrow
#K_RIGHT= right arrow
import pygame, time, sys,os
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

x=20
y=20
bg=pygame.image.load("Images/gameBackground.png") #MAKE MUCH BIGGER
some=pygame.image.load("Images/BadCharacter.png") #MAKE MUCH SMALLER
check =True
while check:
    screen.fill(purple)
    speed=2
    keyBoardKey=pygame.key.get_pressed() #checking what key is pressed
    if keyBoardKey[pygame.K_LEFT]: #moving left on x (-)
        x-=speed
    if keyBoardKey[pygame.K_RIGHT]:
        x +=speed
    if keyBoardKey[pygame.K_UP]: #moving left on x (-)
        y-=speed
    if keyBoardKey[pygame.K_DOWN]:
        y +=speed
    screen.blit(bg,(0,0))#create image on top of other one
    screen.blit(some,(x,y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check = False
pygame.quit()







     