#Deeya Bachani
#We are learning about lists and tuples
#Learn their functions and looping with list

#How to use a module or library by importing
import random
from typing import Counter


myFruit=["apples", "berries", "mangoes", "bananas"]
print(myFruit)
for fruit in myFruit:
    print(fruit)

for fruit in myFruit:
    print(fruit, end= " , ")
print()
Counter=len(myFruit) #length of your list is one more than your last index
indx=random.randint(0,Counter-1)
print("your lucky fruit is", myFruit[indx])

#random method choice()
word=random.choice(myFruit)
print("your random fruit is", word)
for x in range(0,Counter-1):
    print(myFruit[x], end= " , ")

print(myFruit[Counter-1]) #print the last element

if "apples" in myFruit:
    print("Yes, you got apples")
    myFruit.remove("apples")
    print(myFruit)
myFruit.insert(0,"kiwi")
myFruit.insert(2,"papaya")
myFruit.append("beets")
print(myFruit)

fruity=("apple", "pears", "banana") #tuple
print("tuple" , fruity)
temp=list(fruity) #temp is a list
print("list", temp)
temp.insert(1, "kiwi")
fruity=tuple(temp)
print("tuple modified", fruity)
print("list modified", fruity)
for element in fruity:
    print(element)


