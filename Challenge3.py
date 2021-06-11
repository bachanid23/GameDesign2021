#Deeya Bachani
#Challenge 3- list
from typing import List


myColor=["blue", "orange", "yellow", "green", "red"]

l1="My Color Options"
l2="1. insert"
l3="2. delete"
l4="3. find if"
l5="4. find where"
l6="5. reverse"
l7="6. end"
x=1
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print("please enter your selection from 1 to 6")
    inputNumber = input()
    x = int(inputNumber)
    return x

def pause():
    print("Do you want to play again?")
    
    answer1=input()
    answer1=answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False

while x !=6:
    x=menu()
    if (x==1):
        insert=True
        while insert==True:
            myColor.insert(0,"purple")
            print(myColor)
            print("Y/N")
            answer = input()
            if (answer== "Y"):
                        insert=True
            if (answer=="N"):
                        insert=False
            covert=pause()

    if (x==2):
        insert=True
        while insert==True:
            myColor.remove("yellow")
            print(myColor)
            print("Y/N")
            answer = input()
            if (answer== "Y"):
                        insert=True
            if (answer=="N"):
                        insert=False
            covert=pause()

    if (x==3):
        insert=True
        while insert==True:
            print("Write a color name")
            term=str(input())
            if term in myColor:
                print("True")
            else:
                print("False")
            print("Y/N")
            answer = input()
            if (answer== "Y"):
                        insert=True
            if (answer=="N"):
                        insert=False
            covert=pause()


    if (x==4):
        insert=True
        while insert==True:
            print("Find a color")
            x=input()
            myColor.index(x)
            print(myColor.index(x))
            print("Y/N")
            answer = input()
            if (answer== "Y"):
                        insert=True
            if (answer=="N"):
                        insert=False
            covert=pause()

    if (x==5):
        insert=True
        while insert==True:
            myColor.reverse()
            print(myColor)
            print("Y/N")
            answer = input()
            if (answer== "Y"):
                        insert=True
            if (answer=="N"):
                        insert=False
            covert=pause()
print("Goodbye")

