#Deeya Bachani
#While loop instead of if
l1="**************************"
l2="*        My game         *"
l3="* *"
l4="* 1 - Capitalize *"
l5="* 2 - Upper *"
l6="* 3 - Lower *"
l7="* 4 - Find index of char *"
l8="* 5 - Split *"
l9="* 6 - Translate *"
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
    print("please enter your selection from 1 to 5")
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
    print("Press N to continue or Y to stay")
    input()


while x !=4: 
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
            pause()

        
        

    if(x==2):
        print("Level 2 Chosen")
        print("Please enter a phrase")
        answer = input()
        b=answer.upper()
        print(b)
    if(x==3):
        score()
        print("Please enter a phrase")
        answer = input()
        b= answer.swapcase()
        print(b)
    if(x==5):
        print("play with phrase")
        print("Please enter a phrase")
        answer = input()
        myTuple = ("Bob", "Joe", "Emma")
        b=answer.join(myTuple)
        print(b)
print("Goodbye, Thank you for playing")
print("Please enter a phrase")
answer = input()
b=answer.isdigit()
print(b)
