#Deeya Bachani
#Challenge 3
l1="Game Options"
l2="1-insert"
l3="2-remove"
l4=""
l5="* 2 - Upper *"
l6="* 3 - Swapcase *"
l7="* 4 - Count *"
l8="* 5 - myTuple *"
l9="* 6 - Title *"
l10="* 7 - Exit *"
l11="**************************"
x=1 #global variable
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print(l9)
    print(l10)
    print(l11)
    print("please enter your selection from 1 to 7")
    inputNumber = input()
    x = int(inputNumber)
    return x
def score():
    print(11)
    print("* Scores *")
    print(l3)
    print("* 1 - ???- 999 *")
    print("* 2 - ???- 876 *")
    print("* 3 - ???- 745 *")
    print(l3)
    print(l9)
def pause():
    print("Do you want to play again?")
    
    answer1=input()
    answer1=answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False
while x !=7: 
    x=menu()
    if(x==1): #if statement are selection or branching
        capitalize=True
        while capitalize==True:
                print("Level 1 Chosen")
                print("Please enter a phrase")
                answer = input()
                print(answer.capitalize())
                print("Do you want to convert to another string?")
                print("Y/N")
                answer = input()
                if (answer== "Y"):
                        continue
                if (answer=="N"):
                        capitalize=False
                covert= pause()

            
        

    if(x==2):
        upper=True
        while upper==True:
            print("Level 2 Chosen")
            print("Please enter a phrase")
            answer = input()
            print(answer.upper())
            print("Do you want to convert to another string?")
            print("Y/N")
            answer = input()
            if (answer== "Y"):
                        continue
            if (answer=="N"):
                        upper=False
            convert=pause()

    if(x==3):
        swapcase=True
        while swapcase==True:
            print("Level 3 Chosen")
            print("Please enter a phrase")
            answer = input()
            print(answer.swapcase())
            print("Do you want to convert to another string?")
            print("Y/N")
            answer = input()
            if (answer== "Y"):
                        continue
            if (answer=="N"):
                        swapcase=False
            convert=pause()
    if(x==4):
        count=True
        while count==True:
            print("Level 4 Chosen")
            print("Please enter a phrase")
            answer = input()
            print(answer.count("i"))
            print("Do you want to convert to another string?")
            print("Y/N")
            answer = input()
            if (answer== "Y"):
                        count=True
            if (answer=="N"):
                        count=False
            convert=pause()
    if(x==5):
        myTuple=True
        while myTuple==True:
            print("Level 5 chosen")
            print("Please enter a phrase")
            answer = input()
            myTuple = ("Bob", "Joe", "Emma")
            b=answer.join(myTuple)
            print(b)
            print("Do you want to convert to another string?")
            print("Y/N")
            answer = input()
            if (answer== "Y"):
                        myTuple=True
            if (answer=="N"):
                        myTuple=False
            convert=pause()
    if(x==6):
        title=True
        while title==True:
            print("Level 6 chosen")
            print("Please enter a phrase")
            answer = input()
            print(answer.title())
            print("Do you want to convert to another string?")
            print("Y/N")
            answer = input()
            if (answer== "Y"):
                        continue
            if (answer=="N"):
                        title=False
            convert=pause
print("Goodbye, Thank you for playing")