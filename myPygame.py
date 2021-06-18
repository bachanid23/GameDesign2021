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
#create the objects

bg=pygame.image.load("Images/JOYSTICK (2).png")
some=pygame.image.load("Images/background.png")
white=[255, 255, 255]
purple=[200,190,0]
green=[50,25,255]
#create an object to open window
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(purple)
screen.blit(bg,(0,0))#create image on top of other one
pygame.display.set_caption('My Game')#change title on screen and you can also change icon
pygame.display.update() #command to actually do something

check =True
x=10
y=10
rad=30
hbox,wbox=20,20
rect=pygame.Rect(x,y,hbox,wbox)#this creates a rectangle

f=50
j=40
height,width=40,40
rect2=pygame.Rect(f,j,height,width)

Jumpcheck=False
Jump=10


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
#is to check if we are going to jump or not
    if not Jumpcheck:
        if keyBoardKey[pygame.K_UP]: #moving up on y (-)
            rect.y -=speed
        if keyBoardKey[pygame.K_DOWN]:
            rect.y +=speed
        if keyBoardKey[pygame.K_SPACE]:
            Jumpcheck=True
    else:
        if Jump>=-10:
            rect.y -=(Jump* abs(Jump))/2
            Jump-=1
        else:
            Jump=10
            Jumpcheck=False
    if keyBoardKey[pygame.K_s]:
        rad-=speed
    if keyBoardKey[pygame.K_f]:
        rad+=speed
    if keyBoardKey[pygame.K_w]:
        rect2.x -=speed
    if keyBoardKey[pygame.K_r]:
        rect2.x +=speed
    if keyBoardKey[pygame.K_e]:
        rect2.y -=speed
    if keyBoardKey[pygame.K_d]:
        rect2.y +=speed
    if rect.x < 0: rect.x=0
    if rect.x > WIDTH-wbox: rect.x = WIDTH.wbox
    if rect.y < 0: rect.y=0
    if rect.y > HEIGHT-hbox: rect.y = HEIGHT.hbox
    if rect2.x < 0: rect2.x=0
    if rect2.x > WIDTH-width: rect2.x = WIDTH.width
    if rect2.y < 0: rect2.y=0
    if rect2.y > HEIGHT-height: rect2.y = HEIGHT.height
    screen.fill(purple)
    if rad < 0: rad=1
    if rad > WIDTH-x: rad=WIDTH-x
    if rect.colliderect(rect2):
        rect.x -=3
        rect2.x -=3
    screen.fill(purple)
    screen.blit(bg,(0,0))
    screen.blit(some, (rect.x,rect.y))
    pygame.draw.rect(screen,(green),rect)
    pygame.draw.circle(screen,(white), (x+300, y+200), rad,2)
    pygame.draw.rect(screen,(green),rect2)
    pygame.draw.rect(screen,(255,0,0),rect)
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()