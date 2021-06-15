#Deeya Bachani
#6/11/2021
#Word Game
#We are creating a list of words 
#Randomly select a word from the list for the user to guess
#give the user some turns
#show the word to the user with the characters guessed      (add date)
#play the game as long as the user has turns or has guessed the word

import random
from typing import Counter
gamewords= ['python', 'java', 'trackpad', 'computer', 'keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
print("Word Game")
print("1- Play")
print("2- Scores")
print("3- Exit")
choice= input()
while "1" in choice:
    answer=input("Do you want to guess the word?")
    name=input("What is your name?")
    answer=answer.upper()


    def updateWord(word):
        for char in word:
            if char in guesses:
                print(char, end='')
            else:
                print("_", end = " ")

    score=0
    while "Y" in answer:
        guesses= ""
        print("Good luck", name, "!")
        word=random.choice(gamewords)
        updateWord(word)
        counter=len(word)
        turns=10 #should we consider controlling this number
        counter=len(word)
        while turns>0 and counter >0:
            newGuess=input("\n\n Give me a letter ")
            guesses +=newGuess
            if newGuess in word:
                    characters=word.count(newGuess)
                    counter -=characters
                    print("nice guess")
            else:
                    turns -=1
                    print("wrong! you have", turns, "guesses left")
            updateWord(word) 
        print()
        if counter == 0:
            print("You guessed right!")
            score +=1
        else:
            print("Try again next time!")
        answer=input("would you like to play again?").upper()
if "2" in choice:
    import os
    import sys
    filename="WordGameScores.py"
    FILE=open(filename, 'r')
    print(FILE.read())
    FILE.close()

if "3" in choice:
    import os
    import sys
    filename="WordGameExit.py"
    FILE=open(filename, 'r')
    print(FILE.read())
    FILE.close()