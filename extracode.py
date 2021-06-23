import os,sys,time,random,math,time,pygame

pygame.init()

WIDTH=800
HEIGHT=800
WHITE=[255,255,255]
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Game!")
pygame.time.delay(500)
pygame.display.update()

#MAKE MENU
images= []

bg=pygame.image.load("Images/gameBackground.png")
some=pygame.image.load("Images/BadCharacter.png")
screen.blit(bg,(0,0))
screen.blit(some,(5,10))
pygame.time.delay(500)
pygame.display.update()       



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

#is to check if we are going to jump or not
Jumpcheck=False
Jump=10

    if not Jumpcheck:
        if keyBoardKey[pygame.K_UP]: #moving up on y (-)
            some.y -=speed
        if keyBoardKey[pygame.K_DOWN]:
            some.y +=speed
        if keyBoardKey[pygame.K_SPACE]:
            Jumpcheck=True
    else:
        if Jump>=-10:
            some.y -=(Jump* abs(Jump))/2
            Jump-=1
        else:
            Jump=10
            Jumpcheck=False


            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if event.type==QUIT:
                pygame.quit()
                sys.exit()

    
confirm=True
while confirm==True:
    draw_text(text, font, color, surface, x, y)
    main_menu()
    game()
    options()