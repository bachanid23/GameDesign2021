import myPygame, time, sys, pygame

pygame.init()
pygame.time.delay(100)
WIDTH=600
HEIGHT= 400
#create an object to open window
screen=pygame.display.set_mode((WIDTH,HEIGHT))

check =True
while check:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check = False
pygame.quit()