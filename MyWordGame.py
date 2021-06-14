#Deeya Bachani
#6/11/2021
#Word Game
#We are creating a list of words 
#Randomly select a word from the list for the user to guess
#give the user some turns
#show the word to the user with the characters guessed      (add date)
#play the game as long as the user has turns or has guessed the word

import random
gamewords= ['python', 'java', 'trackpad', 'computer', 'keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
#create menu
answer=input("Do you want to guess the word?")
name=input("What is your name?")
answer=answer.upper()
while "Y" in answer:
    print("Good luck", name, "!")
    word=random.choice(gamewords)
    counter=len(word)
    print(counter)
    turns=10 #should we consider controlling this number
    guesses= ""
    while turns>0 and counter >0:
            for char in word:
                if char in guesses:
                    print(char, end='')
                else:
                    print("_", end = " ")
            newGuess=input("\n\n Give me a letter ")
            characters=word.count(newGuess)
            if newGuess not in word:
                turns -=1
                print("wrong! you have", turns, "guesses left")
            else:
                counter -=characters
                print("nice guess")
            guesses += newGuess
               

    answer=input("would you like to play again?").upper()
print(name, " thank you for playing")