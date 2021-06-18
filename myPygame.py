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
WIDTH=600
HEIGHT= 400
white=[255, 255, 255]
purple=[200,190,0]
green=[50,25,255]
#create an object to open window
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(purple)
pygame.display.set_caption('My Game')#change title on screen and you can also change icon
pygame.display.update() #command to actually do something

check =True
x=10
y=10
rad=30
hbox,wbox=20,20
rect=pygame.Rect(x,y,hbox,wbox)#this creates a rectangle


while check:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check = False
    speed=2
    keyBoardKey=pygame.key.get_pressed() #checking what key is pressed
    if keyBoardKey[pygame.K_LEFT]: #moving left on x (-)
        rect.x-=speed
        rad -=speed
    if keyBoardKey[pygame.K_RIGHT]:
        rect.x +=speed
        rad +=speed
    if keyBoardKey[pygame.K_UP]: #moving up on y (-)
        rect.y -=speed
    if keyBoardKey[pygame.K_DOWN]:
        rect.y +=speed
    if keyBoardKey[pygame.K_s]:
        rad-=speed
    if keyBoardKey[pygame.K_f]:
        rad+=speed
    if rect.x < 0: rect, x=0
    if rect.x > WIDTH-wbox: rect.x = WIDTH.wbox
    if rect.y < 0: rect,rect.y=0
    if rect.y > HEIGHT-hbox: rect.y = HEIGHT.hbox
    screen.fill(purple)
    if rad < 0: rad=1
    if rad > WIDTH-x: rad=WIDTH-x
    pygame.draw.rect(screen,(green),rect)
    pygame.draw.circle(screen,(white), (x+300, y+200), rad,2)
    pygame.draw.rect(screen,(green),rect)
    pygame.draw.rect(screen,(255,0,0),rect)
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()