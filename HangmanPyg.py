#Deeya Bachani
#Create a Hangman version of the game:
#Use images in a list Use fonts, render them

from typing import Text
import pygame, math, random, sys, time, os

#os.system('cls')
pygame.init()

#create our screen or window

WIDTH=800
HEIGHT=500
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")

#define colors
WHITE=[255,255,255]
BLACK=[0,0,0]

#load images
images=[]
screen.fill(WHITE)
for i in range(7):
    image=pygame.image.load("ImagesHM\hangman"+str(i)+".png")
    images.append(image)
    #screen.blit(images[i], (100,100))
    #pygame.display.update()
    #pygame.time.delay(500)

#words list
gamewords= ['python', 'java', 'trackpad', 'computer', 'keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
#set up fonts
TitleFont=pygame.font.SysFont("comicsans",70)
WordFont=pygame.font.SysFont("comicsans", 50)
#function to update game and screen
def updateScreen(displayword,turns):
    screen.fill(WHITE)
    screen.blit(images[turns], (80,100))
    pygame.display.update()
    pygame.time.delay(500)
    textW=WordFont.render(displayWord, 1, BLACK)
    screen.blit(textW,(350,150))
    text=TitleFont.render("HANGMAN", 1, BLACK)
    centerTitle=WIDTH/2-text.get_width()/2 #gets the width of my screen/2 - width of our text /2
    screen.blit(text, (centerTitle,20))
    screen.blit(images[turns],(80,100))
    pygame.display.update()
def updateWord(word,guesses): #function with a parameter to update word
    displayWord=""
    for char in word:
        if char in guesses:
            print(char,end=',')
            displayWord+= char+" "
        else:
            displayWord+="_ "
            print('_ ', end =' ')
    return displayWord
check=True
while check:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check=False
    word=random.choice(gamewords)
    guesses=''
    counter=len(word)
    turns=0 #should we consider controlling this number
    displayWord=updateWord(word,guesses)
    updateScreen(displayWord,turns)

    while turns<7 and counter >0:
        newGuess=input("\n\n Give me a letter ")
        #check that the new letter has not been used before
        if newGuess not in guesses:
            if newGuess not in word:
                turns +=1
                print("wrong! you have", turns, "guesses left")
            else:
                counter=word.count(newGuess) #delete repeated letters
                print("nice guess")
            guesses +=newGuess
        else:
            print("you used this one already")
        updateWord(word,guesses) 
pygame.quit()
sys.exit()
