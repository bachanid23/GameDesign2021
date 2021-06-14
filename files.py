#Deeya Bachani
#We are going to learn how to use files
import os
import sys
import time

#using time to pause your game

print("Hello")
time.sleep(2)
print("there")
def readFile():
    file=input("What is the name of the file?")
    if os.path.exists(file): #it is to make sure the file exists
        #It opens the file
        PEN=open(file, 'r')
        #prints the whole file
        print(PEN.read())
        PEN.close
    else:
        print("The file does not exist! Thank you")

fileName="DeeyaGame.txt"
if os.path.exists(fileName):
    print("sorry that file exists")
else:
    FILE=open(fileName,'w')
    FILE.write("***** THIS IS DEEYA'S FILE *****")
    FILE.close()
    time.sleep(1)
    FILE=open(fileName, 'r')
    print(FILE.read())
    FILE.close
File=open("DeeyaGame.txt", 'w')
newLine= "\n What ever    or else"
File.write(newLine)
File.close()